from typing import Optional
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class Room(SQLModel, table=True):
    room_id: Optional[UUID] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    blocked: bool = Field(default=False, index=True)
