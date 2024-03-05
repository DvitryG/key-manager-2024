from uuid import UUID
from fastapi import APIRouter
from backend.models.user import User, Token

router = APIRouter(
    prefix="/users",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_users() -> list[User]:
    pass


@router.post("/register")
async def register() -> Token:
    pass


@router.post("/login")
async def login() -> Token:
    pass


@router.post("/logout")
async def logout():
    pass


@router.get("/me")
async def read_me() -> User:
    pass


@router.put("/me")
async def update_me():
    pass


@router.put("/me/password")
async def update_my_password():
    pass


@router.put("/{user_id}")
async def update_user(user_id: UUID):
    pass
