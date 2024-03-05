# TODO: CRU for orders
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date, datetime, time, timedelta
from dto.OrderDto import SimpleOrder, CyclicOrder


router = APIRouter(
    prefix="/orders",
    tags=["order"],
    responses={404: {"description": "Not found"}},
)

#список заявок пользователя
@router.get("/")
async def get_my_orders():
    pass

#список всех заявок для деканата
@router.get("/all")
async def get_all_orders():
    pass


@router.post("/simple")
async def create_simple_order(order: SimpleOrder):
    pass


@router.post("/cyclic")
async def create_cyclic_order(order: CyclicOrder):
    pass


@router.put("/{order_id}/state")
async def change_order_state():
    pass
