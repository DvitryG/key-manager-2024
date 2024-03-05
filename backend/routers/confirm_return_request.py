from fastapi import APIRouter

router = APIRouter(
    prefix="/confirm_return_requests",
    tags=["confirm_return_request"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_confirm_return_requests():
    pass


@router.put("/{id}")
async def confirm_return():
    pass
