import uuid
from typing import Annotated
from uuid import UUID
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from starlette import status

from backend.dependencies.database import get_db_session
from backend.models.room import Room

router = APIRouter(
    prefix="/rooms",
    tags=["room"],
    responses={404: {"description": "Not found"}},
)


def uuid_generator():
    id = uuid.uuid4()
    return id

async def select_room_by_name(session: Annotated[Session, Depends(get_db_session)], name: str):
    statement = select(Room).where(Room.name==name)
    rooms = session.exec(statement)
    return rooms

async def select_room_by_state( session: Annotated[Session, Depends(get_db_session)], blocked: bool):

    if blocked == True:
        statement = select(Room).where(Room.blocked==True)
    else:
        statement = select(Room).where(Room.blocked==False)
    rooms = session.exec(statement)
    return rooms

async def select_all_rooms_default(session: Annotated[Session, Depends(get_db_session)]):

    statement = select(Room)
    rooms = session.exec(statement).all()
    return rooms

async def select_all_rooms_by_filters(name: str, blocked: bool,
                                      session: Annotated[Session, Depends(get_db_session)]):

    if blocked==True:
        statement = select(Room).where(Room.name==name, Room.blocked==True )
    else:
        statement = select(Room).where(Room.name==name, Room.blocked==False )
    rooms = session.exec(statement)
    return rooms

@router.get("/")
async def get_all_rooms(session: Annotated[Session, Depends(get_db_session)],
                        name: str | None = None, blocked: bool | None = None):
    params = []
    if name is not None:
        params.append(Room.name==name)
    if blocked is not None:
        params.append(Room.blocked==blocked)

    statement = select(Room).where(*params)
    rooms = session.exec(statement)
    rooms = rooms.all()
    return rooms


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
        room = Room(room_id=room_id, name=name) #TODO:проверка на наличие кабинета с занятым названием
        session.add(room)
        session.commit()
    return room.room_id


#TODO:если room_id не найден-> выкинуть ошибку
@router.post("/{room_id}/give/{user_id}")
async def give_room(room_id: UUID, user_id: UUID):
    #если user_id не найден-> выкинуть ошибку

    pass

#TODO:если room_id не найден-> выкинуть ошибку
@router.put("/{room_id}")
async def set_room_availability(room_id: UUID, availability: bool):
    pass

#TODO:если room_id не найден-> выкинуть ошибку
@router.delete("/{room_id}")
async def delete_room(room_id: UUID):
    pass
