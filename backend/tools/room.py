import math
from typing import Annotated, Sequence

from fastapi import Body, Query

from backend.models.common import Pagination
from backend.models.room import Room, RoomsListResponse
from backend.tools.common import FiltersCache


async def paginate_rooms_list(
        rooms: Sequence[Room],
        page: Annotated[int, Query(ge=0)],
        page_size: Annotated[int, Query(ge=1, le=100)],
        rows_count: int
) -> RoomsListResponse:

    page_size = page_size if page_size <= len(rooms) else len(rooms)
    page_size = page_size if page_size > 0 else 1
    pagination = Pagination(page_size=page_size, pages_count=math.ceil(rows_count / page_size), current_page=page)

    return RoomsListResponse(
        rooms=rooms,
        pagination=pagination
    )


class RoomFiltersCache(FiltersCache):
    pass