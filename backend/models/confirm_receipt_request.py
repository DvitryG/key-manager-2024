from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field


class ConfirmReceiptRequest(SQLModel, table=True):
    request_id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID
    room_id: UUID
    order_id: UUID
    confirmed: bool = False
