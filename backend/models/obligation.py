from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import UUID


class Obligation(SQLModel, table=True):
    user_id: UUID = Field(primary_key=True)
    room_id: UUID = Field(primary_key=True)
    deadline: datetime
    closed: bool = Field(default=False, index=True)
