from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    DEAN = "dean"
    TEACHER = "teacher"
    STUDENT = "student"


class User(BaseModel):
    user_id: UUID = uuid4()
    name: str
    email: str
    roles: set[Role]


class UserInDB(User):
    password_hash: str


class Token(BaseModel):
    access_token: str
    token_type: str
