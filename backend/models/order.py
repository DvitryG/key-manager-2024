from typing import Optional, Sequence
from abc import ABC
from sqlmodel import SQLModel, Field
from datetime import date, time
from uuid import UUID, uuid4
from enum import Enum

from backend.models.common import Pagination


class OrderStatus(str, Enum):
    OPENED = "opened"
    APPROVED = "approved"
    CLOSED = "closed"


class Order(SQLModel, table=True):
    order_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(index=True)
    room_id: UUID = Field(index=True, foreign_key="room.room_id")
    status: OrderStatus = Field(default=OrderStatus.OPENED, index=True)

    cyclic: bool = Field(index=True)
    day: date | None = Field(index=True)
    week_day: int | None = Field(index=True)
    start_time: time
    end_time: time


class CreateOrderRequest(SQLModel, ABC):
    room_id: UUID
    start_time: time
    end_time: time


class CreateSimpleOrderRequest(CreateOrderRequest):
    day: date


class CreateCyclicOrderRequest(CreateOrderRequest):
    week_day: int


class OrdersPageResponse(SQLModel):
    orders: Sequence[Order]
    pagination: Pagination
