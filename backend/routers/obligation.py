# TODO: R for Obligations
from fastapi import APIRouter

router = APIRouter(
    prefix="/obligations",
    tags=["obligation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_my_obligations():
    pass
