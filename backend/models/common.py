from sqlmodel import SQLModel


class Pagination(SQLModel):
    page_size: int
    pages_count: int
    current_page: int
