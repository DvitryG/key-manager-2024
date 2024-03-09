from datetime import date, time
from typing import Annotated
from uuid import UUID

from fastapi import Depends
from sqlmodel import Session

from backend.dependencies.database import get_db_session
from backend.models.obligation import Obligation


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
