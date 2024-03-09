from typing import Optional, Sequence
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

from backend.models.common import Pagination
from backend.models.user import User


class Room(SQLModel, table=True):
    room_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True, index=True)
    blocked: bool = Field(default=False, index=True)


class RoomsListResponse(SQLModel):
    rooms: Sequence[Room]
    pagination: Pagination

class Response(SQLModel):
    user: User
    room: Room