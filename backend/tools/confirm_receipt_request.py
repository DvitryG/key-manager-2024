from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import ColumnElement
from sqlmodel import Session, select, or_

from backend.models.confirm_receipt_request import ConfirmReceiptRequest
from backend.models.order import Order, OrderStatus
from backend.models.room import Room
from backend.models.user import User
from backend.tools.order import update_orders_status


def _gen_user_confirm_receipt_requests(
        db_session: Session,
        user: User,
):
    update_orders_status(db_session, user)

    now = datetime.now()
    result = db_session.exec(
        select(Order, Room).where(
            Order.room_id == Room.room_id,
            Room.user_id == None,
            Order.user_id == user.user_id,
            Order.status == OrderStatus.APPROVED,
            or_(
                Order.day == now.date(),
                Order.week_day == now.weekday()
            ),
            Order.end_time > now.time(),
            Order.start_time <= now.time()
        )
    ).all()

    for order, room in result:
        request = ConfirmReceiptRequest(
            user_id=user.user_id,
            room_id=order.room_id,
            deadline=datetime.combine(now.date(), order.end_time)
        )
        db_session.add(request)

        if not order.cyclic:
            order.status = OrderStatus.CLOSED
            db_session.add(order)

    db_session.commit()


def delete_user_old_confirm_receipt_requests(
        db_session: Session,
        user: User,
        request_id: UUID | None = None
):
    clauses = []

    if request_id:
        clauses.append(ConfirmReceiptRequest.request_id == request_id)

    old_requests = db_session.exec(
        select(ConfirmReceiptRequest).where(
            *clauses,
            ConfirmReceiptRequest.user_id == user.user_id,
            ConfirmReceiptRequest.deadline < datetime.now(),

        )
    ).all()

    for request in old_requests:
        db_session.delete(request)

    db_session.commit()


def update_my_confirm_receipt_requests(
        db_session: Session,
        user: User,
        request_id: UUID | None = None
):
    _gen_user_confirm_receipt_requests(db_session, user)
    delete_user_old_confirm_receipt_requests(db_session, user, request_id)
