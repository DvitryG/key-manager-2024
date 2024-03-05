from sqlmodel import SQLModel
from uuid import UUID


class ConfirmReturnRequest(SQLModel):
    room_id: UUID
    confirmed: bool = False
