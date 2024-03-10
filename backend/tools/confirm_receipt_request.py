from datetime import datetime, timedelta
from uuid import UUID

from sqlmodel import Session, select, or_

from backend.models.confirm_receipt_request import ConfirmReceiptRequest
from backend.models.order import Order, OrderStatus
from backend.models.room import Room
from backend.models.user import User
from backend.tools.order import update_orders_status, get_user_active_orders_with_room


def create_user_confirm_receipt_request(
        db_session: Session,
        user: User,
        room: Room,
        order: Order | None = None
):
    now = datetime.now()
    if not order:
        new_receipt_request = ConfirmReceiptRequest(
            user_id=user.user_id,
            room_id=room.room_id,
            deadline=now + timedelta(minutes=5)
        )
    else:
        new_receipt_request = ConfirmReceiptRequest(
            user_id=user.user_id,
            room_id=room.room_id,
            deadline=datetime.combine(now.date(), order.end_time)
        )
        if not order.cyclic:
            order.status = OrderStatus.CLOSED
            db_session.add(order)

    db_session.add(new_receipt_request)
    db_session.commit()


def delete_user_irrelevant_confirm_receipt_requests(
        db_session: Session,
        user: User,
        request_id: UUID | None = None
):
    clauses = []

    if request_id:
        clauses.append(ConfirmReceiptRequest.request_id == request_id)

    irrelevant_requests = db_session.exec(
        select(ConfirmReceiptRequest, Room).where(
            *clauses,
            ConfirmReceiptRequest.room_id == Room.room_id,
            ConfirmReceiptRequest.user_id == user.user_id,
            or_(
                ConfirmReceiptRequest.deadline < datetime.now(),
                Room.blocked == True
            )

        )
    ).all()

    for request in irrelevant_requests:
        db_session.delete(request)

    db_session.commit()


def update_my_confirm_receipt_requests(
        db_session: Session,
        user: User,
        request_id: UUID | None = None
):
    update_orders_status(db_session, user)
    delete_user_irrelevant_confirm_receipt_requests(db_session, user, request_id)

    for order, room in get_user_active_orders_with_room(db_session, user):
        create_user_confirm_receipt_request(db_session, user, room, order)

    db_session.commit()
