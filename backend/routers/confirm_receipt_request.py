from http.client import HTTPException
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from starlette import status

from backend.dependencies.database import get_db_session
from backend.dependencies.user import authorize, get_current_user
from backend.models.confirm_receipt_request import ConfirmReceiptRequest
from backend.models.user import User

router = APIRouter(
    prefix="/confirm_receipt_requests",
    tags=["confirm_receipt_request"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", dependencies=[Depends(
    authorize()
)])
async def get_my_confirm_receipt_requests(
        db_session: Annotated[Session, Depends(get_db_session)],
        current_user: Annotated[User, Depends(get_current_user)]
) -> list[ConfirmReceiptRequest]:
    requests = db_session.exec(select(ConfirmReceiptRequest)
                               .where(ConfirmReceiptRequest.user_id == current_user.user_id,
                                      ConfirmReceiptRequest.confirmed == False)
                               ).all()
    return requests


@router.put("/{request_id}", dependencies=[Depends(
    authorize()
)])
async def confirm_receipt(
        db_session: Annotated[Session, Depends(get_db_session)],
        request_id: UUID
):
    request = db_session.get(ConfirmReceiptRequest, request_id)
    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The request with request_id: {request_id} not found in the system."
        )

    request.confirmed = True
    db_session.add(request)
    db_session.commit()
