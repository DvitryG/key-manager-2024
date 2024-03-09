from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, Query, HTTPException
from uuid import UUID
from sqlmodel import Session, select, or_
from backend.dependencies.database import get_db_session
from backend.dependencies.user import get_current_user, authorize
from backend.models.common import Pagination
from backend.models.room import Room

from backend.models.user import User, Role
from backend.models.order import (
    Order,
    OrderStatus,
    CreateSimpleOrderRequest,
    CreateCyclicOrderRequest,
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
            Order.day == day,
            Order.week_day == day.weekday()
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
        user_id: UUID = None,
        day: date | None = None,
        order_status: Annotated[OrderStatus | None, Query()] = None,
        blocked: bool | None = None,
        room_id: UUID = None,
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
            Order.day == day,
            Order.week_day == day.weekday()
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
        order: CreateSimpleOrderRequest
) -> Order:
    new_order = Order(
        user_id=user.user_id,
        **order.model_dump()
    )
    db_session.add(new_order)
    db_session.commit()

    return new_order


@router.post("/cyclic", dependencies=[Depends(
    authorize(Role.TEACHER)
)])
async def create_cyclic_order(
        db_session: Annotated[Session, Depends(get_db_session)],
        user: Annotated[User, Depends(get_current_user)],
        order: CreateCyclicOrderRequest
) -> Order:
    new_order = Order(
        user_id=user.user_id,
        **order.model_dump()
    )
    db_session.add(new_order)
    db_session.commit()

    return new_order


@router.put("/{order_id}/state")
async def change_order_state(
        db_session: Annotated[Session, Depends(get_db_session)],
        user: Annotated[User, Depends(get_current_user)],
        order_id: UUID,
        state: OrderStatus
):
    order = (db_session.get(Order, order_id))

    if order.user_id != user.user_id and not user.roles & {Role.ADMIN, Role.DEAN}:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = state
    db_session.add(order)
    db_session.commit()
