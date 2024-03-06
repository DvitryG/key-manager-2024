from sqlmodel import SQLModel, Field
from uuid import UUID


class ConfirmReceiptRequest(SQLModel, table=True):
    user_id: UUID = Field(primary_key=True)
    room_id: UUID = Field(primary_key=True)
    confirmed: bool = False
