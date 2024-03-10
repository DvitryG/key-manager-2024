from typing import Annotated, Sequence
from uuid import UUID
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select

from backend.dependencies.database import get_db_session
from backend.dependencies.order import get_room_by_id
from backend.dependencies.user import authorize
from backend.models.common import Pagination
from backend.models.confirm_return_request import ConfirmReturnRequestPage
from backend.models.room import Room, CurrentRoomUserResponse
from backend.models.user import Role, UserInDB
from backend.tools.common import get_pages_count_from_cache
from backend.tools.confirm_return_request import ConfirmReturnRequestFiltersCache

router = APIRouter(
    prefix="/confirm_return_requests",
    tags=["confirm_return_request"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", dependencies=[Depends(
    authorize(Role.ADMIN, Role.DEAN)
)])
async def get_all_confirm_return_requests(
        db_session: Annotated[Session, Depends(get_db_session)],
        user_id: UUID | None = None,
        room_id: UUID | None = None,
        page: Annotated[int, Query(ge=0)] = 0,
        page_size: Annotated[int, Query(ge=1)] = 10
) -> ConfirmReturnRequestPage:
    filters = [Room.user_id == UserInDB.user_id]

    if user_id:
        filters.append(UserInDB.user_id == user_id)

    if room_id:
        filters.append(Room.room_id == room_id)

    result = db_session.exec(
        select(Room, UserInDB).where(
            *filters
        ).offset(page * page_size).limit(page_size)
    ).all()

    rooms_users = []
    for room, user in result:
        rooms_users.append(CurrentRoomUserResponse(
            room=room,
            user=user
        ))

    pages_count = await get_pages_count_from_cache(
        lambda: db_session.query(UserInDB).where(*filters).count(),
        ConfirmReturnRequestFiltersCache,
        {"user_id": user_id, "room_id": room_id, "page_size": page_size}
    )

    return ConfirmReturnRequestPage(
        requests=rooms_users,
        pagination=Pagination(
            page_size=len(rooms_users),
            pages_count=pages_count,
            current_page=page
        )
    )


@router.delete("/{room_id}", dependencies=[Depends(
    authorize(Role.ADMIN, Role.DEAN)
)])
async def confirm_return(
        db_session: Annotated[Session, Depends(get_db_session)],
        room: Annotated[Room, Depends(get_room_by_id)],
):
    room.user_id = None

    db_session.add(room)
    db_session.commit()

    return True

