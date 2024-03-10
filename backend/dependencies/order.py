from datetime import time, date, datetime
from typing import Annotated
from uuid import UUID

from fastapi import Depends, Body, HTTPException
from sqlmodel import Session

from backend.dependencies.database import get_db_session
from backend.models.order import Order


def get_order_by_id(
    db_session: Annotated[Session, Depends(get_db_session)],
    order_id: UUID
) -> Order:
    order = db_session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


def get_valid_time_range(
    start_time: Annotated[time, Body()],
    end_time: Annotated[time, Body()]
) -> tuple[time, time]:
    if end_time < start_time:
        raise HTTPException(status_code=400, detail="End time must be after start time")
    return start_time, end_time


def get_valid_week_day(
    week_day: Annotated[int, Body()]
) -> int:
    if week_day < 0 or week_day > 5:
        raise HTTPException(status_code=400, detail="Week day must be between 0 and 5")
    return week_day


def get_valid_day(
    day: Annotated[date, Body()]
) -> date:
    if day < date.today():
        raise HTTPException(status_code=400, detail="Date must be in the future")
    return day


def get_valid_day_and_time(
    day: Annotated[date, Depends(get_valid_day)],
    time_range: Annotated[tuple[time, time], Depends(get_valid_time_range)]
) -> tuple[date, time, time]:
    start_time, end_time = time_range
    now = datetime.now()
    print(now)
    if day == now.date() and start_time < now.time():
        raise HTTPException(status_code=400, detail="Time must be in the future")
    return day, start_time, end_time
