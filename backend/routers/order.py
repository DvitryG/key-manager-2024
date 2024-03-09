from datetime import date, time
from typing import Annotated

from fastapi import APIRouter, Depends, Query, HTTPException
from uuid import UUID
from sqlmodel import Session, select, or_
from backend.dependencies.database import get_db_session
from backend.dependencies.order import (
    get_valid_time_range,
    get_verified_room_id,
    get_valid_week_day,
    get_valid_day,
    get_order_by_id
)
from backend.dependencies.user import get_current_user, authorize
from backend.models.common import Pagination
from backend.models.room import Room

from backend.models.user import User, Role
from backend.models.order import (
    Order,
    OrderStatus,
    OrdersPageResponse
)
from backend.tools.common import get_pages_count_from_cache
from backend.tools.order import OrderFiltersCache

router = APIRouter(
    prefix="/orders",
    tags=["order"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", dependencies=[Depends(
    authorize(Role.STUDENT, Role.TEACHER)
)])
async def get_my_orders(
        db_session: Annotated[Session, Depends(get_db_session)],
        user: Annotated[User, Depends(get_current_user)],
        day: date | None = None,
        room_id: UUID = None,
        page: Annotated[int, Query(ge=0)] = 0,
        page_size: Annotated[int, Query(ge=1, le=100)] = 10
) -> OrdersPageResponse:
    order_filters = [Order.user_id == user.user_id]

    if day:
        order_filters.append(or_(
            Order.week_day == day.weekday(),
            Order.day == day
        ))

    if room_id:
        order_filters.append(Order.room_id == room_id)

    orders = db_session.exec(
        select(Order)
        .offset(page * page_size).limit(page_size)
        .where(*order_filters)
    ).all()

    pages_count = await get_pages_count_from_cache(
        lambda: db_session.query(Order).where(*order_filters).count(),
        OrderFiltersCache,
        {
            "day": day,
            "room_id": str(room_id),
            "page_size": page_size,
        }
    )

    return OrdersPageResponse(
        orders=orders,
        pagination=Pagination(
            page_size=len(orders),
            pages_count=pages_count,
            current_page=page
        )
    )


@router.get("/all", dependencies=[Depends(
    authorize(Role.ADMIN, Role.DEAN)
)])
async def get_all_orders(
        db_session: Annotated[Session, Depends(get_db_session)],
        user_id: UUID | None = None,
        day: date | None = None,
        order_status: Annotated[OrderStatus | None, Query()] = None,
        blocked: bool | None = None,
        room_id: UUID | None = None,
        page: Annotated[int, Query(ge=0)] = 0,
        page_size: Annotated[int, Query(ge=1, le=100)] = 10
) -> OrdersPageResponse:
    order_filters = []

    if user_id:
        order_filters.append(Order.user_id == str(user_id))

    if order_status is not None:
        order_filters.append(Order.status == order_status)

    if day:
        order_filters.append(or_(
            Order.week_day == day.weekday(),
            Order.day == day
        ))

    if blocked is not None:
        order_filters.append(Room.blocked == blocked)

    if room_id:
        order_filters.append(Order.room_id == room_id)

    result = db_session.exec(
        select(Order, Room)
        .where(Order.room_id == Room.room_id)
        .offset(page * page_size).limit(page_size)
        .where(*order_filters)
    ).all()

    orders = tuple(zip(*result))[0] if result else []

    pages_count = await get_pages_count_from_cache(
        lambda: db_session.query(Order, Room).where(
            Order.room_id == Room.room_id, *order_filters
        ).count(),
        OrderFiltersCache,
        {
            "day": day,
            "order_status": order_status,
            "blocked": blocked,
            "user_id": user_id,
            "room_id": str(room_id),
            "page_size": page_size,
        }
    )

    return OrdersPageResponse(
        orders=orders,
        pagination=Pagination(
            page_size=len(orders),
            pages_count=pages_count,
            current_page=page
        )
    )


@router.post("/simple", dependencies=[Depends(
    authorize(Role.STUDENT, Role.TEACHER)
)])
async def create_simple_order(
        db_session: Annotated[Session, Depends(get_db_session)],
        user: Annotated[User, Depends(get_current_user)],
        room_id: Annotated[UUID, Depends(get_verified_room_id)],
        time_range: Annotated[tuple[time, time], Depends(get_valid_time_range)],
        day: Annotated[date, Depends(get_valid_day)],
) -> Order:
    start_time, end_time = time_range

    overlapping_order = db_session.exec(
        select(Order).where(
            Order.status == OrderStatus.APPROVED,
            Order.room_id == room_id,
            or_(
                Order.week_day == day.weekday(),
                Order.day == day
            ),
            Order.start_time > start_time,
            Order.end_time < end_time
        )
    ).first()

    if overlapping_order:
        raise HTTPException(status_code=400, detail="The room has already been booked for this time")

    new_order = Order(
        user_id=user.user_id,
        room_id=room_id,
        cyclic=False,
        day=day,
        start_time=start_time,
        end_time=end_time
    )
    db_session.add(new_order)
    db_session.commit()
    OrderFiltersCache.clear()

    db_session.refresh(new_order)
    return new_order


@router.post("/cyclic", dependencies=[Depends(
    authorize(Role.TEACHER)
)])
async def create_cyclic_order(
        db_session: Annotated[Session, Depends(get_db_session)],
        user: Annotated[User, Depends(get_current_user)],
        room_id: Annotated[UUID, Depends(get_verified_room_id)],
        time_range: Annotated[tuple[time, time], Depends(get_valid_time_range)],
        week_day: Annotated[int, Depends(get_valid_week_day)],
) -> Order:
    start_time, end_time = time_range

    overlapping_order = db_session.exec(
        select(Order).where(
            Order.status == OrderStatus.APPROVED,
            Order.room_id == room_id,
            Order.week_day == week_day,
            Order.start_time > start_time,
            Order.end_time < end_time
        )
    ).first()

    if overlapping_order:
        raise HTTPException(status_code=400, detail="The room has already been booked for this time")

    new_order = Order(
        user_id=user.user_id,
        room_id=room_id,
        cyclic=True,
        week_day=week_day,
        start_time=start_time,
        end_time=end_time
    )
    db_session.add(new_order)
    db_session.commit()
    OrderFiltersCache.clear()

    db_session.refresh(new_order)
    return new_order


@router.put("/{order_id}/approve", dependencies=[Depends(
    authorize(Role.DEAN, Role.ADMIN)
)])
async def approve_order(
        db_session: Annotated[Session, Depends(get_db_session)],
        order: Annotated[Order, Depends(get_order_by_id)],
):
    if order.status != OrderStatus.OPENED:
        raise HTTPException(status_code=400, detail="The order is already approved or closed")

    order.status = OrderStatus.APPROVED
    db_session.add(order)
    db_session.commit()
    OrderFiltersCache.clear()


@router.put("/{order_id}/close", dependencies=[Depends(
    authorize()
)])
async def close_order(
        db_session: Annotated[Session, Depends(get_db_session)],
        user: Annotated[User, Depends(get_current_user)],
        order: Annotated[Order, Depends(get_order_by_id)],
):
    if order.user_id != user.user_id and not user.roles & {Role.ADMIN, Role.DEAN}:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    if order.status == OrderStatus.CLOSED:
        raise HTTPException(status_code=400, detail="The order is already closed")

    order.status = OrderStatus.CLOSED
    db_session.add(order)
    db_session.commit()
    OrderFiltersCache.clear()
