from abc import ABC
from pydantic import BaseModel
from datetime import date, time
from uuid import UUID, uuid4
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


class Order(BaseModel, ABC):
    order_id: UUID = uuid4()
    user_id: UUID
    room_id: UUID
    start_time: time
    end_time: time
    status: OrderStatus = OrderStatus.IN_PROGRESS
    blocked: bool = False


class SimpleOrder(Order):
    date: date


class CyclicOrder(Order):
    week_day: int
