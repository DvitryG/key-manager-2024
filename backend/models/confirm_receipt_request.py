from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

from backend.models.room import Room
from backend.models.user import User


class ConfirmReceiptRequest(SQLModel, table=True):
    request_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(index=True, foreign_key="userindb.user_id")
    room_id: UUID = Field(index=True, foreign_key="room.room_id")
    deadline: datetime = Field(index=True)


class ConfirmReceiptRequestResponse(SQLModel):
    request_id: UUID
    user: User
    room: Room
    deadline: datetime
