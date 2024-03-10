from typing import Optional
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

from backend.models.user import User


class Room(SQLModel, table=True):
    room_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True)
    user_id: Optional[UUID] = Field(default=None, index=True, foreign_key="userindb.user_id")


class CurrentRoomUserResponse(SQLModel):
    room: Room
    user: User
