from typing import Optional
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4
from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    DEAN = "dean"
    TEACHER = "teacher"
    STUDENT = "student"


class User(SQLModel):
    user_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(unique=True, index=True)
    roles_str: str = Field(default='', index=True)

    @staticmethod
    def roles_to_str(roles: list[Role]) -> str:
        return ",".join([role.value for role in sorted(roles)])

    @property
    def roles(self) -> list[Role]:
        return [Role(role) for role in self.roles_str.split(",")]

    @roles.setter
    def roles(self, roles: list[Role]):
        self.roles_str = User.roles_to_str(roles)


class UserInDB(User, table=True):
    password_hash: str


class UserSession(SQLModel, table=True):
    session_id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID


class Token(SQLModel):
    access_token: str
    token_type: str


class LoginRequest(SQLModel):
    email: str
    password: str
