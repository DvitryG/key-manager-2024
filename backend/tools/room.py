from difflib import SequenceMatcher

from backend.tools.common import FiltersCache


def is_similar_room_name(room_name: str, search_name: str) -> bool:
    return SequenceMatcher(None, room_name, search_name).ratio() > 0.6


class RoomFiltersCache(FiltersCache):
    pass
