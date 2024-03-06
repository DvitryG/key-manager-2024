from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from uuid import UUID
from sqlmodel import Session, select
from backend.dependencies.database import get_db_session
from backend.dependencies.user import get_user

from backend.models.user import User
from backend.models.order import (
    Order,
    SimpleOrder,
    CyclicOrder,
    OrderStatus,
    CreateSimpleOrderRequest,
    CreateCyclicOrderRequest,
    OrdersListsResponse
)


router = APIRouter(
    prefix="/orders",
    tags=["order"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_my_orders(
        user: Annotated[User, Depends(get_user)],
        db_session: Annotated[Session, Depends(get_db_session)]
) -> OrdersListsResponse:
    simple_orders = db_session.exec(
        select(SimpleOrder).where(Order.user_id == user.user_id)
    )
    cyclic_orders = db_session.exec(
        select(CyclicOrder).where(Order.user_id == user.user_id)
    )
    return OrdersListsResponse(
        simple_orders=simple_orders.all(),
        cyclic_orders=cyclic_orders.all()
    )


@router.get("/all")
async def get_all_orders(
        db_session: Annotated[Session, Depends(get_db_session)],
        user_id: UUID = None,
        day: date | None = None,
        order_status: Annotated[OrderStatus | None, Query()] = None,
        blocked: bool | None = None,
        room_id: UUID = None,
) -> OrdersListsResponse:
    simple_order_filters = []
    cyclic_order_filters = []

    if user_id:
        simple_order_filters.append(SimpleOrder.user_id == str(user_id))
        cyclic_order_filters.append(CyclicOrder.user_id == str(user_id))

    if order_status is not None:
        simple_order_filters.append(SimpleOrder.status == order_status)
        cyclic_order_filters.append(CyclicOrder.status == order_status)

    if day:
        simple_order_filters.append(SimpleOrder.day == day)
        cyclic_order_filters.append(CyclicOrder.week_day == day.weekday())

    if blocked is not None:
        simple_order_filters.append(SimpleOrder.blocked == blocked)
        cyclic_order_filters.append(CyclicOrder.blocked == blocked)

    if room_id:
        simple_order_filters.append(SimpleOrder.room_id == room_id)
        cyclic_order_filters.append(CyclicOrder.room_id == room_id)

    simple_orders = db_session.exec(
        select(SimpleOrder).where(*simple_order_filters)
    )
    cyclic_orders = db_session.exec(
        select(CyclicOrder).where(*cyclic_order_filters)
    )

    return OrdersListsResponse(
        simple_orders=simple_orders.all(),
        cyclic_orders=cyclic_orders.all()
    )


@router.post("/simple")
async def create_simple_order(
        user: Annotated[User, Depends(get_user)],
        db_session: Annotated[Session, Depends(get_db_session)],
        order: CreateSimpleOrderRequest
) -> SimpleOrder:
    new_order = SimpleOrder(
        user_id=user.user_id,
        **order.model_dump()
    )
    db_session.add(new_order)
    db_session.commit()

    return new_order


@router.post("/cyclic")
async def create_cyclic_order(
        user: Annotated[User, Depends(get_user)],
        db_session: Annotated[Session, Depends(get_db_session)],
        order: CreateCyclicOrderRequest
) -> CyclicOrder:
    new_order = CyclicOrder(
        user_id=user.user_id,
        **order.model_dump()
    )
    db_session.add(new_order)
    db_session.commit()

    return new_order


@router.put("/{order_id}/state")
async def change_order_state(
        db_session: Annotated[Session, Depends(get_db_session)],
        order_id: UUID,
        state: OrderStatus
):
    order = (db_session.get(SimpleOrder, order_id) or
             db_session.get(CyclicOrder, order_id))
    if not order:
        raise ValueError("Order not found") #  TODO: change to 404
    order.status = state
    db_session.add(order)
    db_session.commit()
