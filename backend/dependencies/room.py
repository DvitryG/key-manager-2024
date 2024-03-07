from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException
from sqlmodel import Session
from starlette import status

from backend.dependencies.database import get_db_session
from backend.models.room import Room


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
