from typing import Optional, Sequence
from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field, Relationship

from backend.models.common import Pagination
from backend.models.obligation import Obligation
from backend.models.user import User


class Room(SQLModel, table=True):
    room_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True, index=True)
    blocked: bool = Field(default=False, index=True)
    obligations: list[Obligation] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}
    )


class RoomsListResponse(SQLModel):
    rooms: Sequence[Room]
    pagination: Pagination


class Response(SQLModel):
    user: User
    room: Room
