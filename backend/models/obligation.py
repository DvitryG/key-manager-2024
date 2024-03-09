from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field


class Obligation(SQLModel, table=True):
    user_id: UUID = Field(primary_key=True)
    room_id: UUID = Field(primary_key=True, foreign_key="room.room_id")
    deadline: datetime
    closed: bool = Field(default=False, index=True)

