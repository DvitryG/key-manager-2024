from abc import ABC
from pydantic import BaseModel
from uuid import UUID, uuid4


class Room(BaseModel, ABC):
    room_id: UUID = uuid4()
    name: str
    blocked: bool = False
