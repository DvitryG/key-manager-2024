from typing import Optional
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class Room(SQLModel, table=True):
    room_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True)
    blocked: bool = Field(default=False, index=True)
