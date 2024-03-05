from sqlmodel import SQLModel
from uuid import UUID


class ConfirmReceiptRequest(SQLModel):
    room_id: UUID
    user_id: UUID
    confirmed: bool = False
