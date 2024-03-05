from abc import ABC
from sqlmodel import SQLModel
from uuid import UUID, uuid4


class Room(SQLModel, ABC):
    room_id: UUID = uuid4()
    name: str
    blocked: bool = False
