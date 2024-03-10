from typing import Annotated, Sequence
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Body, Query
from sqlmodel import Session, select
from starlette import status

from backend.dependencies.database import get_db_session
from backend.dependencies.room import get_room_by_id
from backend.dependencies.obligation import get_current_user_obligation
from backend.dependencies.user import get_user_by_id
from backend.dependencies.user import authorize, get_current_user
from backend.models.common import Pagination
from backend.models.obligation import Obligation
from backend.models.room import Room, RoomsListResponse
from backend.models.user import User, Role, UserInDB
from backend.tools.common import get_filtered_items, get_pages_count_from_cache, get_filtered_count
from backend.tools.confirm_receipt_request import create_new_receipt_request
from backend.tools.room import is_similar_room_name, RoomFiltersCache

router = APIRouter(
    prefix="/rooms",
    tags=["room"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", dependencies=[Depends(authorize(Role.DEAN, Role.ADMIN))])
async def get_all_rooms(
        db_session: Annotated[Session, Depends(get_db_session)],
        name: Annotated[str | None, Query()] = None,
        page: Annotated[int, Query(ge=0)] = 0,
        page_size: Annotated[int, Query(ge=1, le=100)] = 10,
        blocked: bool | None = None
) -> RoomsListResponse:
    filters = []

    if blocked is not None:
        filters.append(Room.blocked == blocked)

    rooms = await get_filtered_items(
        db_session, Room, lambda room: is_similar_room_name(room.name, name),
        *filters,
        offset=page * page_size, limit=page_size
    ) if name else db_session.exec(
        select(Room).where(*filters).offset(page * page_size).limit(page_size).order_by(Room.name)
    ).all()

    pages_count = await get_pages_count_from_cache(
        lambda: get_filtered_count(
            db_session, Room, lambda room: is_similar_room_name(room.name, name),
            *filters
        ) if name else db_session.query(Room).where(*filters).count(),
        RoomFiltersCache,
        {"name": name, "page_size": page_size, "blocked": blocked}
    )

    return RoomsListResponse(
        rooms=rooms,
        pagination=Pagination(
            page_size=len(rooms),
            pages_count=pages_count,
            current_page=page,
        )
    )


@router.get("/search", dependencies=[Depends(
    authorize()
)])
async def get_rooms_by_name(
        db_session: Annotated[Session, Depends(get_db_session)],
        name: Annotated[str | None, Query()] = None,
        limit: Annotated[int, Query(ge=1, le=100)] = 10
) -> Sequence[Room]:

    rooms = await get_filtered_items(
        db_session, Room, lambda user: is_similar_room_name(user.name, name),
        limit=limit
    ) if name else db_session.exec(
        select(Room).limit(limit).order_by(Room.name)
    ).all()

    return rooms


@router.post("/", dependencies=[Depends(
    authorize(Role.ADMIN, Role.DEAN))
])
async def create_room(
        name: Annotated[str, Body(min_length=3, max_length=50)],
        db_session: Annotated[Session, Depends(get_db_session)]
) -> UUID:
    overlapping_room = db_session.exec(select(Room).where(Room.name == name))
    if overlapping_room.first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The room with name:{name} already exists in the system."
        )

    room = Room(name=name)
    db_session.add(room)
    db_session.commit()
    db_session.refresh(room)
    RoomFiltersCache.clear()
    return room.room_id


@router.post("/{room_id}/give/{user_id}", dependencies=[Depends(
    authorize(Role.STUDENT, Role.TEACHER))
])
async def give_room(
        current_user: Annotated[User, Depends(get_current_user)],
        room: Annotated[Room, Depends(get_room_by_id)],
        user: Annotated[UserInDB, Depends(get_user_by_id)],
        db_session: Annotated[Session, Depends(get_db_session)]
) -> UUID:

    get_current_user_obligation(current_user.user_id, room.room_id, db_session)

    new_receipt_request = create_new_receipt_request(
        user.user_id,
        room.room_id,
        db_session
    )
    return new_receipt_request.request_id


@router.put("/{room_id}", dependencies=[Depends(authorize(Role.ADMIN, Role.DEAN))])
async def set_room_availability(
        room: Annotated[Room, Depends(get_room_by_id)],
        availability: bool,
        db_session: Annotated[Session, Depends(get_db_session)]
) -> Room:
    room.blocked = availability
    db_session.add(room)
    db_session.commit()

    db_session.refresh(room)
    RoomFiltersCache.clear()
    return room


@router.delete("/{room_id}", dependencies=[Depends(authorize(Role.ADMIN, Role.DEAN))])
async def delete_room(
        room: Annotated[Room, Depends(get_room_by_id)],
        db_session: Annotated[Session, Depends(get_db_session)]
):

    db_session.delete(room)
    db_session.commit()
    RoomFiltersCache.clear()
