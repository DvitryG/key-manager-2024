from http.client import HTTPException
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlmodel import Session
from starlette import status

from backend.dependencies.database import get_db_session
from backend.dependencies.order import get_order_by_id
from backend.dependencies.user import authorize, get_current_user
from backend.models.confirm_receipt_request import ConfirmReceiptRequest
from backend.models.user import User
from backend.tools.obligation import create_new_obligation

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
    requests = db_session.get(ConfirmReceiptRequest, current_user.user_id).all()
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

    # ищем заявку по order_id указанного в request
    order = get_order_by_id(db_session, request.order_id)
    # создаем новое обязательство для пользователя с user_id указанным в request
    new_obligation = create_new_obligation(
        db_session,
        order.user_id,
        order.room_id,
        order.day,
        order.end_time
    )

    return new_obligation

