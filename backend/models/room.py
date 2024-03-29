from typing import Optional, Sequence
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

from backend.models.common import Pagination
from backend.models.user import User


class Room(SQLModel, table=True):
    room_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True)
    user_id: Optional[UUID] = Field(default=None, index=True, foreign_key="userindb.user_id")
    blocked: bool = Field(default=False, index=True)


class CurrentRoomUserResponse(SQLModel):
    room: Room
    user: User


class RoomsListResponse(SQLModel):
    rooms: Sequence[Room]
    pagination: Pagination
