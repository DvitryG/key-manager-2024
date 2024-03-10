from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, Body
from sqlmodel import Session

from backend.dependencies.database import get_db_session
from backend.models.room import Room


def get_room_by_id(
    db_session: Annotated[Session, Depends(get_db_session)],
    room_id: UUID
):
    room = db_session.get(Room, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


def get_room_by_id_in_body(
    db_session: Annotated[Session, Depends(get_db_session)],
    room_id: Annotated[UUID, Body()]
):
    return get_room_by_id(db_session, room_id)




