from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException
from sqlmodel import Session
from starlette import status

from backend.dependencies.database import get_db_session
from backend.models.obligation import Obligation
from backend.models.room import Room
from backend.models.user import UserInDB


def get_room_by_id(
        room_id: UUID,
        db_session: Annotated[Session, Depends(get_db_session)]
) -> Room:
    room = db_session.get(Room, room_id)
    if room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The room with room_id: {room_id} not found in the system."
        )
    return room


def get_user_by_id(
        user_id: UUID,
        db_session: Annotated[Session, Depends(get_db_session)]
) -> UserInDB:
    user = db_session.get(UserInDB, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user with user_id: {user_id} not found in the system."
        )
    return user


def get_obligation_by_user_id(
        user_id: UUID,
        room_id: UUID,
        db_session: Annotated[Session, Depends(get_db_session)]
) -> Obligation:

    obligation = db_session.get(Obligation, (user_id, room_id))

    if obligation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The obligation was not found in the system."
        )
    return obligation

