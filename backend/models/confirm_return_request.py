from pydantic import BaseModel
from uuid import UUID


class ConfirmReturnRequest(BaseModel):
    room_id: UUID
    confirmed: bool = False
