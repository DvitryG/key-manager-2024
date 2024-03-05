from datetime import time
from fastapi import APIRouter
from uuid import UUID
from backend.models.order import (
    SimpleOrder,
    CyclicOrder,
    OrderStatus,
    Interval
)


router = APIRouter(
    prefix="/orders",
    tags=["order"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_my_orders() -> list[SimpleOrder | CyclicOrder]:
    pass


@router.get("/all")
async def get_all_orders() -> list[SimpleOrder | CyclicOrder]:
    pass


@router.post("/simple")
async def create_simple_order(order: SimpleOrder):
    pass


@router.post("/cyclic")
async def create_cyclic_order(order: CyclicOrder):
    pass


@router.put("/{order_id}/state")
async def change_order_state(order_id: UUID, state: OrderStatus):
    pass


@router.get("/intervals")
async def get_intervals() -> dict[Interval, tuple[time, time]]:
    pass
