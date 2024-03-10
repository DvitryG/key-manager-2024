from typing import Sequence, Annotated

from fastapi import APIRouter, Depends
from sqlmodel import select, Session

from backend.dependencies.database import get_db_session
from backend.dependencies.user import authorize, get_current_user
from backend.models.room import CurrentRoomUserResponse, Room
from backend.models.user import Role, UserInDB, User

router = APIRouter(
    prefix="/obligations",
    tags=["obligation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", dependencies=[Depends(
    authorize(Role.STUDENT, Role.TEACHER)
)])
async def get_my_obligations(
        db_session: Annotated[Session, Depends(get_db_session)],
        user: Annotated[User, Depends(get_current_user)],
) -> Sequence[CurrentRoomUserResponse]:
    result = db_session.exec(
        select(Room, UserInDB).where(
            Room.user_id == UserInDB.user_id,
            UserInDB.user_id == user.user_id
        )
    ).all()

    rooms_users = []
    for room, user in result:
        rooms_users.append(CurrentRoomUserResponse(
            room=room,
            user=user
        ))

    return rooms_users
