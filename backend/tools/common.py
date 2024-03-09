from typing import TypeVar, Sequence, Type, Coroutine

from sqlalchemy import BinaryExpression
from sqlmodel import SQLModel, Session, select

from backend.constants import FILTER_BATCH_SIZE

_I = TypeVar("_I", bound=SQLModel)


async def _get_filtered_batch(
        n_batch: int,
        db_session: Session,
        table: Type[_I],
        filter_algorithm: callable,
        *where_filters: BinaryExpression,
) -> list[_I]:
    return list(filter(
        filter_algorithm,
        db_session.exec(
            select(table)
            .offset(n_batch * FILTER_BATCH_SIZE)
            .limit(FILTER_BATCH_SIZE)
            .where(*where_filters)
        ).all()))


async def get_filtered_items(
        db_session: Session,
        table: Type[_I],
        filter_algorithm: callable,
        *where_filters: BinaryExpression,
        offset: int = 0,
        limit: int | None = None
) -> Sequence[_I]:
    """
    Фильтрует набор элементов таблицы по алгоритму

    :param db_session: сессия БД
    :param table: тип таблицы, к которой будет применяться фильтр
    :param filter_algorithm: алгоритм фильтрации, принимает элемент таблицы и возвращает bool
    :param where_filters: стандартные фильтры в sql запросе
    :param offset: сколько элементов нужно пропустить (по умолчанию 0)
    :param limit: сколько элементов нужно найти (по умолчанию все)
    :return: набор элементов таблицы, прошедших фильтры
    """
    target_items = []
    skipped_count = 0

    items_count = db_session.query(table).count()
    batch_count = items_count // FILTER_BATCH_SIZE + (items_count % FILTER_BATCH_SIZE > 0)

    for batch in range(batch_count):
        if limit is not None and len(target_items) >= limit:
            break
        items = await _get_filtered_batch(
            batch, db_session, table, filter_algorithm, *where_filters
        )
        not_skipped_items = items[offset - skipped_count:]
        skipped_count += len(items) - len(not_skipped_items)
        target_items += not_skipped_items

    return target_items


async def get_filtered_count(
        db_session: Session,
        table: Type[_I],
        filter_algorithm: callable,
        *where_filters: BinaryExpression
) -> int:
    target_items_count = 0

    items_count = db_session.query(table).count()
    batch_count = items_count // FILTER_BATCH_SIZE + (items_count % FILTER_BATCH_SIZE > 0)

    for batch in range(batch_count):
        target_items_count += len(await _get_filtered_batch(
            batch, db_session, table, filter_algorithm, *where_filters
        ))

    return target_items_count


class FiltersCache:
    __filters_cache: dict[str, dict] = {}

    @staticmethod
    def _get_key(filter_data: dict[str, str]) -> str:
        return ''.join(sorted(
            f'{str(key)}:{str(value)}' for key, value in filter_data.items()
        ))

    @classmethod
    def get(cls, filter_data: dict[str, str]):
        return cls.__filters_cache.get(cls._get_key(filter_data))

    @classmethod
    def update(cls, filter_data: dict[str, str], value: dict):
        cls.__filters_cache.setdefault(cls._get_key(filter_data), {}).update(value)

    @classmethod
    def clear(cls):
        cls.__filters_cache.clear()


async def get_pages_count_from_cache(
        get_items_count: callable,
        cache: Type[FiltersCache],
        filter_data: dict,
) -> int:
    cache_data = cache.get(filter_data)
    page_count = cache_data and cache_data.get('page_count')

    if not page_count:
        items_count = get_items_count()
        if isinstance(items_count, Coroutine):
            items_count = await items_count
        page_count = items_count // filter_data['page_size'] + (items_count % filter_data['page_size'] > 0)
        cache.update(filter_data, {'page_count': page_count})

    return page_count
