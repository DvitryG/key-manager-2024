from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from backend.dependencies.database import get_db_session
from backend.dependencies.user import get_current_user, authorize
from backend.models.obligation import Obligation
from backend.models.user import User, Role

router = APIRouter(
    prefix="/obligations",
    tags=["obligation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/my")
async def get_my_obligations(
        db_session: Annotated[Session, Depends(get_db_session)],
        current_user: Annotated[User, Depends(get_current_user)]
) -> list[Obligation]:
    obligations = db_session.exec(
        select(Obligation).where(Obligation.user_id == current_user.user_id)
    ).all()

    return obligations
