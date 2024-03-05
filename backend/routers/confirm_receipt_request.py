from uuid import UUID
from fastapi import APIRouter
from backend.models.confirm_receipt_request import ConfirmReceiptRequest

router = APIRouter(
    prefix="/confirm_receipt_requests",
    tags=["confirm_receipt_request"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_my_confirm_receipt_requests() -> list[ConfirmReceiptRequest]:
    pass


@router.put("/{request_id}")
async def confirm_receipt(request_id: UUID):
    pass
