from uuid import UUID
from fastapi import APIRouter
from backend.models.room import Room

router = APIRouter(
    prefix="/rooms",
    tags=["room"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_rooms() -> list[Room]:
    pass


@router.post("/")
async def create_room() -> Room:
    pass


@router.post("/{room_id}/give/{user_id}")
async def give_room(room_id: UUID, user_id: UUID):
    pass


@router.put("/{room_id}")
async def set_room_availability(room_id: UUID, availability: bool):
    pass


@router.delete("/{room_id}")
async def delete_room(room_id: UUID):
    pass
