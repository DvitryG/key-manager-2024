from datetime import time, date
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
    Interval,
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
        order_status: Annotated[list[OrderStatus] | None, Query()] = None,
        blocked: bool | None = None,
        room_id: UUID = None,
) -> OrdersListsResponse:
    filters = []
    if user_id:
        filters.append(Order.user_id == user_id)
    if order_status is not None:
        filters.append(Order.status in order_status)
    if blocked is not None:
        filters.append(Order.blocked == blocked)
    if room_id:
        filters.append(Order.room_id == room_id)

    simple_order_filters = filters.copy()
    cyclic_order_filters = filters.copy()
    if day:
        simple_order_filters.append(SimpleOrder.day == day)
        cyclic_order_filters.append(CyclicOrder.week_day == day.weekday())

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
async def create_simple_order(order: CreateSimpleOrderRequest):
    pass


@router.post("/cyclic")
async def create_cyclic_order(order: CreateCyclicOrderRequest):
    pass


@router.put("/{order_id}/state")
async def change_order_state(order_id: UUID, state: OrderStatus):
    pass


@router.get("/intervals")
async def get_intervals() -> dict[Interval, tuple[time, time]]:
    pass
