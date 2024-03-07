#TODO[Dima]:добавить проверку на авторизацию и наличие прав
import math
from typing import Annotated
from uuid import UUID
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from starlette import status

from backend.dependencies.database import get_db_session
from backend.models.room import Room, RoomsListResponse, Pagination

router = APIRouter(
    prefix="/rooms",
    tags=["room"],
    responses={404: {"description": "Not found"}},
)


def uuid_generator():
    id = uuid.uuid4()
    return id


@router.get("/")#TODO:добавить пагинацию
async def get_all_rooms(session: Annotated[Session, Depends(get_db_session)],
                        name: str | None = None,
                        page: int | None = 1,
                        size: int | None = 6,
                        blocked: bool | None = None) -> RoomsListResponse:
    params = []
    if name is not None:
        params.append(Room.name==name)
    if blocked is not None:
        params.append(Room.blocked==blocked)

    statement = select(Room).where(*params)
    rooms = session.exec(statement).all()
    rooms.sort(key = lambda room: room.name)

    paginated_list = []
    size = size if size <= len(rooms) else len(rooms)
    start_index = size * (page-1)
    last_index = start_index + size if start_index + size <= len(rooms) else len(rooms)

    for i in range(start_index, last_index):
        paginated_list.append(rooms[i])
    size = size if size > 0 else 1
    pagination = Pagination(size= size, count=math.ceil(len(rooms)/size), current=page)

    return RoomsListResponse(
        rooms=paginated_list,
        pagination=pagination
    )


@router.post("/")
async def create_room(name: str,
                      room_id: Annotated[UUID, Depends(uuid_generator)],
                      session: Annotated[Session, Depends(get_db_session)]):
    room = session.exec(select(Room).where(Room.name==name))
    if room.all():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The room with name:{name} already exists in the system."
        )
    else:
        room = Room(room_id=room_id, name=name)
        session.add(room)
        session.commit()
    return room.room_id


#TODO:если room_id не найден-> выкинуть ошибку
@router.post("/{room_id}/give/{user_id}")
async def give_room(room_id: UUID, user_id: UUID):
    #если user_id не найден-> выкинуть ошибку

    pass


@router.put("/{room_id}")
async def set_room_availability(room_id: UUID, availability: bool,
                                session: Annotated[Session, Depends(get_db_session)]):
    result = session.exec(select(Room).where(Room.room_id==room_id))
    room = result.first()
    if room is not None:
        room.blocked = availability
        session.add(room)
        session.commit()
        session.refresh(room)
        return room.room_id
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The room with room_id: {room_id} doesn't exist in the system."
        )


@router.delete("/{room_id}")
async def delete_room(room_id: UUID,
                      session: Annotated[Session, Depends(get_db_session)]):
    result = session.exec(select(Room).where(Room.room_id == room_id))
    room = result.first()
    if room is not None:
        session.delete(room)
        session.commit()
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The room with room_id: {room_id} not found in the system."
        )
