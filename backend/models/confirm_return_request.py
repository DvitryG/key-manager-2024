from typing import Sequence

from sqlmodel import SQLModel
from uuid import UUID

from backend.models.common import Pagination
from backend.models.room import CurrentRoomUserResponse


class ConfirmReturnRequestPage(SQLModel):
    requests: Sequence[CurrentRoomUserResponse]
    pagination: Pagination
