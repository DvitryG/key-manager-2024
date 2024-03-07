import math
from typing import Annotated, Sequence

from fastapi import Body

from backend.models.room import Room, RoomsListResponse, Pagination


async def paginate_rooms_list(
        rooms: Sequence[Room],
        page: Annotated[int, Body(ge=0)],
        page_size: Annotated[int, Body(ge=1, le=100)]
) -> RoomsListResponse:
    paginated_list = []
    size = page_size if page_size <= len(rooms) else len(rooms)
    start_index = size * (page - 1)
    last_index = start_index + size if start_index + size <= len(rooms) else len(rooms)

    for i in range(start_index, last_index):
        paginated_list.append(rooms[i])
    size = size if size > 0 else 1
    pagination = Pagination(size=size, count=math.ceil(len(rooms) / size), current=page)

    return RoomsListResponse(
        rooms=paginated_list,
        pagination=pagination
    )
