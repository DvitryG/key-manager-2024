from typing import TypeVar, Sequence, Type

from sqlalchemy import BinaryExpression
from sqlmodel import SQLModel, Session, select

from backend.constants import FILTER_BATCH_SIZE

_I = TypeVar("_I", bound=SQLModel)


async def custom_db_filter(
        db_session: Session,
        table: Type[_I],
        filter_algorithm: callable,
        *where_filters: BinaryExpression,
        required_count: int | None = None
) -> Sequence[_I]:
    """
    Фильтрует набор элементов таблицы по алгоритму

    :param db_session: сессия БД
    :param table: тип таблицы, к которой будет применяться фильтр
    :param filter_algorithm: алгоритм фильтрации, принимает элемент таблицы и возвращает bool
    :param required_count: сколько элементов нужно найти (по умолчанию все)
    :param where_filters: стандартные фильтры в sql запросе
    :return: набор элементов таблицы, прошедших фильтры
    """
    target_items = []

    items_count = db_session.query(table).count()
    batch_count = items_count // FILTER_BATCH_SIZE + (items_count % FILTER_BATCH_SIZE > 0)

    for batch in range(batch_count):
        if required_count is not None and len(target_items) >= required_count:
            break
        target_items += filter(
            filter_algorithm,
            db_session.exec(
                select(table)
                .offset(batch * FILTER_BATCH_SIZE)
                .limit(FILTER_BATCH_SIZE)
                .where(*where_filters)
            ).all()
        )

    return target_items
