import math
from typing import Annotated, Sequence

from fastapi import Body, Query

from backend.models.room import Room, RoomsListResponse, Pagination


async def paginate_rooms_list(
        rooms: Sequence[Room],
        page: Annotated[int, Query(ge=0)],
        page_size: Annotated[int, Query(ge=1, le=100)],
        rows_count: int
) -> RoomsListResponse:

    page_size = page_size if page_size <= len(rooms) else len(rooms)
    page_size = page_size if page_size > 0 else 1
    pagination = Pagination(size=page_size, count=math.ceil(rows_count / page_size), current=page)

    return RoomsListResponse(
        rooms=rooms,
        pagination=pagination
    )