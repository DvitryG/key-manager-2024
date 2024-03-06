from typing import Optional, Sequence
from abc import ABC
from sqlmodel import SQLModel, Field
from datetime import date, time
from uuid import UUID, uuid4
from enum import Enum


class OrderStatus(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    APPROVED = "APPROVED"
    CLOSED = "CLOSED"


class Order(SQLModel, ABC):
    order_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(index=True)
    room_id: UUID = Field(index=True)
    start_time: time
    end_time: time
    status: OrderStatus = Field(default=OrderStatus.IN_PROGRESS, index=True)
    blocked: bool = Field(default=False, index=True)


class SimpleOrder(Order, table=True):
    day: date = Field(index=True)


class CyclicOrder(Order, table=True):
    week_day: int = Field(index=True)


class CreateOrderRequest(SQLModel, ABC):
    room_id: UUID
    start_time: time
    end_time: time


class CreateSimpleOrderRequest(CreateOrderRequest):
    day: date


class CreateCyclicOrderRequest(CreateOrderRequest):
    week_day: int


class OrdersListsResponse(SQLModel):
    simple_orders: Sequence[SimpleOrder]
    cyclic_orders: Sequence[CyclicOrder]
