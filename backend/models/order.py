from typing import Optional
from abc import ABC
from sqlmodel import SQLModel, Field
from datetime import date, time
from uuid import UUID
from enum import Enum


class OrderStatus(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    APPROVED = "APPROVED"
    CLOSED = "CLOSED"


class Interval(str, Enum):
    first_lesson = "first_lesson"
    first_break = "first_break"
    second_lesson = "second_lesson"
    second_break = "second_break"
    third_lesson = "third_lesson"
    third_break = "third_break"
    fourth_lesson = "fourth_lesson"
    fourth_break = "fourth_break"
    fifth_lesson = "fifth_lesson"
    fifth_break = "fifth_break"
    sixth_lesson = "sixth_lesson"


class Order(SQLModel, ABC):
    order_id: Optional[UUID] = Field(default=None, primary_key=True)
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
