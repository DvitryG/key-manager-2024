from datetime import datetime, timezone
from typing import Sequence
from uuid import UUID

from sqlalchemy import ColumnElement
from sqlmodel import select, or_, and_, Session

from backend.models.order import Order, OrderStatus
from backend.models.room import Room
from backend.models.user import User
from backend.tools.common import FiltersCache


def update_orders_status(
        db_session: Session,
        user: User | None = None,
):
    clauses = []

    if user:
        clauses.append(Order.user_id == user.user_id)

    now = datetime.now()
    old_orders = db_session.exec(
        select(Order).where(
            *clauses,
            Order.status != OrderStatus.CLOSED,
            or_(
                and_(Order.day == now.date(), Order.end_time < now.time()),
                Order.day < now.date()
            )
        )
    ).all()

    for order in old_orders:
        order.status = OrderStatus.CLOSED
        db_session.add(order)

    db_session.commit()


def get_user_active_orders_with_room(
        db_session: Session,
        user: User,
        current_room_owner_id: UUID | None = None
) -> Sequence[tuple[Order, Room]]:
    now = datetime.now()

    result = db_session.exec(
        select(Order, Room).where(
            Order.room_id == Room.room_id,
            Order.user_id == user.user_id,
            Room.user_id == current_room_owner_id,
            Order.status == OrderStatus.APPROVED,
            or_(
                Order.day == now.date(),
                Order.week_day == now.weekday()
            ),
            Order.end_time > now.time(),
            Order.start_time <= now.time()
        )
    ).all()

    return result


class OrderFiltersCache(FiltersCache):
    pass
