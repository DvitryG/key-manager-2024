# TODO[Dima]:добавить проверку на авторизацию и наличие прав
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlmodel import Session, select
from starlette import status

from backend.dependencies.database import get_db_session
from backend.dependencies.room import get_room_by_id
from backend.models.room import Room, RoomsListResponse
from backend.tools.room import paginate_rooms_list

router = APIRouter(
    prefix="/rooms",
    tags=["room"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_rooms(
        db_session: Annotated[Session, Depends(get_db_session)],
        name: str | None = None,
        page: int | None = 1,
        size: int | None = 6,
        blocked: bool | None = None
) -> RoomsListResponse:
    params = []
    if name is not None:
        params.append(Room.name == name)
    if blocked is not None:
        params.append(Room.blocked == blocked)

    statement = select(Room).where(*params)
    rooms = db_session.exec(statement).all()
    rooms.sort(key=lambda room: room.name)

    rooms = await paginate_rooms_list(rooms, size, page)
    return rooms


#TODO:сделать генерацию id в конструкторе
@router.post("/")
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


# TODO:если room_id не найден-> выкинуть ошибку
@router.post("/{room_id}/give/{user_id}")
async def give_room(room_id: UUID, user_id: UUID):
    # если user_id не найден-> выкинуть ошибку

    pass


@router.put("/{room_id}")
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


@router.delete("/{room_id}")
async def delete_room(
        room: Annotated[Room, Depends(get_room_by_id)],
        db_session: Annotated[Session, Depends(get_db_session)]
):
    db_session.delete(room)
    db_session.commit()
