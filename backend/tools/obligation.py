from datetime import date, time
from typing import Annotated, Sequence
from uuid import UUID

from fastapi import Depends
from sqlmodel import Session, SQLModel

from backend.dependencies.database import get_db_session
from backend.models.common import Pagination
from backend.models.confirm_receipt_request import ConfirmReceiptRequest
from backend.models.obligation import Obligation
from backend.tools.common import FiltersCache


def create_new_obligation(
        db_session: Annotated[Session, Depends(get_db_session)],
        user_id: UUID,
        room_id: UUID,
        day: date,
        end_time: time
) -> Obligation:
    deadline = day +'T'+ end_time
    new_obligation = Obligation(
        user_id=user_id,
        room_id=room_id,
        deadline=deadline
    )
    db_session.add(new_obligation)
    db_session.commit()

    return new_obligation


class RequestsListResponse(SQLModel):
    requests: Sequence[ConfirmReceiptRequest]
    pagination: Pagination


class RequestsCache(FiltersCache):
    pass
