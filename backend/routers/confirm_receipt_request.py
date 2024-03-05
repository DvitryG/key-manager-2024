from fastapi import APIRouter

router = APIRouter(
    prefix="/confirm_receipt_requests",
    tags=["confirm_receipt_request"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_my_confirm_receipt_requests():
    pass


@router.put("/{id}")
async def confirm_receipt():
    pass
