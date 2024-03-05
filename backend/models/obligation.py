from sqlmodel import SQLModel
from datetime import datetime
from uuid import UUID


class Obligation(SQLModel):
    user_id: UUID
    room_id: UUID
    deadline: datetime
    closed: bool = False
