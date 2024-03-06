from sqlmodel import SQLModel
from uuid import UUID


# Не таблица в базе данных, запрашиваем все room с user_id != None
class ConfirmReturnRequest(SQLModel):
    room_id: UUID
    user_id: UUID
