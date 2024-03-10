from typing import Annotated
from uuid import UUID

from fastapi import Depends
from sqlmodel import Session

from backend.dependencies.database import get_db_session
from backend.models.confirm_receipt_request import ConfirmReceiptRequest


def create_new_receipt_request(
    user_id: UUID,
    room_id: UUID,
    db_session: Annotated[Session, Depends(get_db_session)]
) -> ConfirmReceiptRequest:
    new_request = ConfirmReceiptRequest(
        user_id=user_id,
        room_id=room_id
    )
    db_session.add(new_request)
    db_session.commit()
    db_session.refresh(new_request)
    return new_request