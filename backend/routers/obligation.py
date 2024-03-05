from fastapi import APIRouter
from backend.models.obligation import Obligation

router = APIRouter(
    prefix="/obligations",
    tags=["obligation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_my_obligations() -> list[Obligation]:
    pass
