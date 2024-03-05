from pydantic import BaseModel
from uuid import UUID


class ConfirmReceiptRequest(BaseModel):
    room_id: UUID
    user_id: UUID
    confirmed: bool = False
