from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlmodel import Session

from backend.dependencies.database import get_db_session
from backend.dependencies.user import authorize
from backend.models.confirm_return_request import ConfirmReturnRequest
from backend.models.user import Role

router = APIRouter(
    prefix="/confirm_return_requests",
    tags=["confirm_return_request"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", dependencies=[Depends(
    authorize(Role.ADMIN, Role.DEAN))
])
async def get_all_confirm_return_requests(
        db_session: Annotated[Session, Depends(get_db_session)],

) -> list[ConfirmReturnRequest]:
    pass


@router.put("/{request_id}")
async def confirm_return(request_id: UUID):
    pass
