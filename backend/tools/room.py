import math
from difflib import SequenceMatcher
from itertools import product
from typing import Annotated, Sequence

from fastapi import Body, Query

from backend.models.common import Pagination
from backend.models.room import Room, RoomsListResponse
from backend.tools.common import FiltersCache


async def paginate_rooms_list(
        rooms: Sequence[Room],
        current_page: Annotated[int, Query(ge=1)],
        page_size: Annotated[int, Query(ge=1, le=100)],
        rows_count: int
) -> RoomsListResponse:

    size = page_size
    size = size if size > 0 else 1
    pagination = Pagination(page_size=page_size, pages_count=math.ceil(rows_count / size), current_page=current_page)

    return RoomsListResponse(
        rooms=rooms,
        pagination=pagination
    )


def is_similar_room_name(room_name: str, search_name: str) -> bool:
    return SequenceMatcher(None, room_name, search_name).ratio() > 0.6


class RoomFiltersCache(FiltersCache):
    pass
