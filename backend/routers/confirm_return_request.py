from uuid import UUID
from fastapi import APIRouter
from backend.models.confirm_return_request import ConfirmReturnRequest

router = APIRouter(
    prefix="/confirm_return_requests",
    tags=["confirm_return_request"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_confirm_return_requests() -> list[ConfirmReturnRequest]:
    pass


@router.put("/{request_id}")
async def confirm_return(request_id: UUID):
    pass
