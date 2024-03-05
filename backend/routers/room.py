# TODO: CRUD for rooms
from fastapi import APIRouter

router = APIRouter(
    prefix="/rooms",
    tags=["room"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_rooms():
    pass


@router.post("/")
async def create_room():
    pass


@router.post("/{room_id}/give/{user_id}")
async def give_room():
    pass


@router.put("/{room_id}")
async def set_room_availability():
    pass


@router.delete("/{room_id}")
async def delete_room():
    pass
