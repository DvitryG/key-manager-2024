from typing import Optional
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4
from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    DEAN = "dean"
    TEACHER = "teacher"
    STUDENT = "student"


class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    #roles: set[Role]

# class User(BaseModel):
#     user_id: UUID = uuid4()
#     name: str
#     email: str
#     roles: set[Role]


class UserInDB(User):
    password_hash: str


class Token(SQLModel):
    access_token: str
    token_type: str
