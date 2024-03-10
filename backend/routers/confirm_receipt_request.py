from datetime import date
from typing import Annotated, Sequence
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, or_

from backend.dependencies.database import get_db_session
from backend.dependencies.user import authorize, get_current_user
from backend.models.confirm_receipt_request import ConfirmReceiptRequest, ConfirmReceiptRequestResponse
from backend.models.room import Room
from backend.models.user import Role, User, UserInDB
from backend.tools.confirm_receipt_request import (
    update_my_confirm_receipt_requests,
    delete_user_irrelevant_confirm_receipt_requests
)

router = APIRouter(
    prefix="/confirm_receipt_requests",
    tags=["confirm_receipt_request"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", dependencies=[Depends(
    authorize(Role.STUDENT, Role.TEACHER)
)])
async def get_my_confirm_receipt_requests(
        db_session: Annotated[Session, Depends(get_db_session)],
        user: Annotated[User, Depends(get_current_user)],
        room_id: UUID | None = None,
        day: date | None = None,
) -> Sequence[ConfirmReceiptRequestResponse]:
    update_my_confirm_receipt_requests(db_session, user)

    filters = [
        ConfirmReceiptRequest.user_id == UserInDB.user_id,
        ConfirmReceiptRequest.room_id == Room.room_id
    ]

    if room_id:
        filters.append(ConfirmReceiptRequest.room_id == room_id)

    if day:
        filters.append(or_(
            ConfirmReceiptRequest.week_day == day.weekday(),
            ConfirmReceiptRequest.day == day
        ))

    result = db_session.exec(
        select(ConfirmReceiptRequest, UserInDB, Room).where(*filters)
    ).all()

    requests = []
    for request, user, room in result:
        requests.append(ConfirmReceiptRequestResponse(
            **request.model_dump(exclude={'user_id', 'room_id'}),
            user=user,
            room=room
        ))

    return requests


@router.delete("/{request_id}", dependencies=[Depends(
    authorize(Role.STUDENT, Role.TEACHER)
)])
async def confirm_receipt(
        db_session: Annotated[Session, Depends(get_db_session)],
        user: Annotated[User, Depends(get_current_user)],
        request_id: UUID,
        confirm: bool
) -> bool:
    delete_user_irrelevant_confirm_receipt_requests(
        db_session, user, request_id
    )

    request = db_session.get(ConfirmReceiptRequest, request_id)

    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    if request.user_id != user.user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    if confirm:
        room = db_session.get(Room, request.room_id)

        if not room:
            raise HTTPException(status_code=404, detail="Room not found")

        room.user_id = user.user_id
        db_session.add(room)

    db_session.delete(request)
    db_session.commit()

    return True
