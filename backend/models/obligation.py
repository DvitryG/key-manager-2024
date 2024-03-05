from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class Obligation(BaseModel):
    user_id: UUID
    room_id: UUID
    deadline: datetime
    closed: bool = False
