from typing import Annotated

from fastapi import Depends, HTTPException
from sqlmodel import Session
from starlette import status

from backend.dependencies.database import get_db_session
from backend.dependencies.room import get_room_by_id
from backend.dependencies.user import get_current_user
from backend.models.obligation import Obligation
from backend.models.room import Room
from backend.models.user import User


def get_current_user_obligation(
        db_session: Annotated[Session, Depends(get_db_session)],
        user: Annotated[User, Depends(get_current_user)],
        room: Annotated[Room, Depends(get_room_by_id)],
) -> Obligation:

    obligation = db_session.get(Obligation, (user.user_id, room.room_id))

    if obligation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The obligation was not found in the system."
        )
    return obligation
