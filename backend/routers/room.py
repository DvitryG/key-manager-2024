from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Body, Query
from sqlalchemy import func
from sqlmodel import Session, select
from starlette import status

from backend.dependencies.database import get_db_session
from backend.dependencies.room import get_room_by_id, get_user_by_id, get_obligation_by_user_id
from backend.dependencies.user import authorize, get_current_user
from backend.models.common import Pagination
from backend.models.obligation import Obligation
from backend.models.room import Room, RoomsListResponse
from backend.models.user import User, Role, UserInDB
from backend.tools.common import get_filtered_count, get_filtered_items
from backend.tools.room import paginate_rooms_list, RoomFiltersCache
from backend.tools.user import UserFiltersCache, is_similar_usernames

router = APIRouter(
    prefix="/rooms",
    tags=["room"],
    responses={404: {"description": "Not found"}},
)


# TODO:подправить пагинацию
@router.get("/", dependencies=[Depends(authorize(Role.STUDENT, Role.TEACHER, Role.DEAN, Role.ADMIN))])
async def get_all_rooms(
        db_session: Annotated[Session, Depends(get_db_session)],
        current_page: Annotated[int, Query(ge=1)] = 1,
        page_size: Annotated[int, Query(ge=1, le=100)] = 10,
        blocked: bool | None = None
) -> RoomsListResponse:
    params = []

    if blocked is not None:
        params.append(Room.blocked == blocked)
    rooms_count = 0
    statement = select(Room).where(*params).offset((current_page-1) * page_size).limit(page_size).order_by(Room.name)
    rooms = db_session.exec(statement).all()
    if len(params) != 0:
        rooms_count = db_session.query(Room).where(Room.blocked == blocked).count()
    else:
        rooms_count = db_session.exec(
            select(func.count(Room.room_id))
        ).first()

    rooms = await paginate_rooms_list(rooms, current_page, page_size, rooms_count)
    return rooms


@router.get("/search", dependencies=[Depends(authorize(Role.STUDENT, Role.TEACHER, Role.DEAN, Role.ADMIN))])
async def get_rooms_by_name(
        db_session: Annotated[Session, Depends(get_db_session)],
        name: Annotated[str | None, Query()] = None,
        page: Annotated[int, Query(ge=0)] = 0,
        page_size: Annotated[int, Query(ge=1, le=100)] = 10
) -> RoomsListResponse:
    filter_data = {"name": name, "page_size": page_size}
    cache = UserFiltersCache.get(filter_data)
    page_count = cache and cache.get('page_count')

    if not page_count:
        items_count = await get_filtered_count(
            db_session, Room, lambda room: is_similar_usernames(room.name, name)
        ) if name else db_session.query(Room).count()

        page_count = items_count // page_size + (items_count % page_size > 0)
        RoomFiltersCache.update(filter_data, {'page_count': page_count})

    rooms = await get_filtered_items(
        db_session, Room, lambda user: is_similar_usernames(user.name, name),
        offset=page * page_size, limit=page_size
    ) if name else db_session.exec(
        select(Room).offset(page * page_size).limit(page_size).order_by(Room.name)
    ).all()

    return RoomsListResponse(
        rooms=rooms,
        pagination=Pagination(
            page_size=len(rooms),
            pages_count=page_count,
            current_page=page,
        )
    )


@router.post("/", dependencies=[Depends(authorize(Role.ADMIN, Role.DEAN))])
async def create_room(
        name: Annotated[str, Body(min_length=3, max_length=50)],
        db_session: Annotated[Session, Depends(get_db_session)]
) -> UUID:
    room = db_session.exec(select(Room).where(Room.name == name))
    if room.first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The room with name:{name} already exists in the system."
        )

    room = Room(name=name)
    db_session.add(room)
    db_session.commit()

    return room.room_id


@router.post("/{room_id}/give/{user_id}",
             dependencies=[Depends(authorize(Role.STUDENT, Role.TEACHER, Role.DEAN, Role.ADMIN))]
             )
async def give_room(
        current_user: Annotated[User, Depends(get_current_user)],
        room: Annotated[Room, Depends(get_room_by_id)],
        user: Annotated[UserInDB, Depends(get_user_by_id)],
        db_session: Annotated[Session, Depends(get_db_session)]
):
    current_obligation = get_obligation_by_user_id(current_user.user_id, room.room_id, db_session)

    new_obligation = Obligation(
        user_id=user.user_id,
        deadline=current_obligation.deadline,
        room_id=room.room_id,
        closed=False
    )
    db_session.add(new_obligation)
    db_session.commit()

    db_session.delete(current_obligation)
    db_session.commit()


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
    return room


@router.delete("/{room_id}", dependencies=[Depends(authorize(Role.ADMIN, Role.DEAN))])
async def delete_room(
        room: Annotated[Room, Depends(get_room_by_id)],
        db_session: Annotated[Session, Depends(get_db_session)]
):
    db_session.delete(room)
    db_session.commit()
