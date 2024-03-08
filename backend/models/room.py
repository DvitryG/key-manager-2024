from typing import Optional, Sequence
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class Room(SQLModel, table=True):
    room_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True, index=True)
    blocked: bool = Field(default=False, index=True)


class Pagination(SQLModel):
    size: int = 6
    count: int = 0
    current: int = 0


class RoomsListResponse(SQLModel):
    rooms: Sequence[Room]
    pagination: Pagination

