from datetime import datetime, timezone

from sqlalchemy import ColumnElement
from sqlmodel import select, or_, and_, Session

from backend.models.order import Order, OrderStatus
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


class OrderFiltersCache(FiltersCache):
    pass
