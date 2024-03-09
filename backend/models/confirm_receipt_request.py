from datetime import date, time
from typing import Optional

from sqlmodel import SQLModel, Field
from uuid import UUID


class ConfirmReceiptRequest(SQLModel, table=True):
    user_id: UUID = Field(primary_key=True)
    room_id: UUID = Field(primary_key=True)
    order_id: UUID = Field(index=True, foreign_key="order.order_id")
    confirmed: bool = False
