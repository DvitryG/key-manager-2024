# TODO: CRU for orders
from fastapi import APIRouter

router = APIRouter(
    prefix="/orders",
    tags=["order"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_my_orders():
    pass


@router.get("/all")
async def get_all_orders():
    pass


@router.post("/simple")
async def create_simple_order():
    pass


@router.post("/cyclic")
async def create_cyclic_order():
    pass


@router.put("/{order_id}/state")
async def change_order_state():
    pass
