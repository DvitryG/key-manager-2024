from typing import Annotated, Sequence
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Body, Query
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from backend.dependencies.database import get_db_session
from backend.dependencies.user import (
    get_current_user,
    get_verified_email,
    get_validated_password,
    get_current_user_session
)
from backend.models.user import (
    User,
    Token,
    UserInDB,
    LoginRequest,
    Role,
    UserSession
)
from backend.tools.user import (
    hash_password,
    authenticate_user,
    verify_password
)

router = APIRouter(
    prefix="/users",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all_users(
        db_session: Annotated[Session, Depends(get_db_session)],
        name: Annotated[str | None, Query()] = None,
        page: Annotated[int, Query(ge=0)] = 0,
        page_size: Annotated[int, Query(ge=1, le=100)] = 10
) -> Sequence[User]:
    # TODO: add filter by name
    return db_session.exec(
        select(UserInDB).offset(page * page_size).limit(page_size)
    ).all()


@router.post("/register")
async def register(
        db_session: Annotated[Session, Depends(get_db_session)],
        email: Annotated[str, Depends(get_verified_email)],
        name: Annotated[str, Body(min_length=3, max_length=64)],
        password: Annotated[str, Depends(get_validated_password)],
        repeat_password: Annotated[str, Body()]
) -> Token:
    if password != repeat_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    user = UserInDB(
        email=email,
        name=name,
        password_hash=hash_password(password),
    )
    db_session.add(user)
    db_session.commit()

    return authenticate_user(db_session, email, password)


@router.post("/login")
async def login(
        db_session: Annotated[Session, Depends(get_db_session)],
        login_data: LoginRequest
) -> Token:
    return authenticate_user(
        db_session,
        email=login_data.email,
        password=login_data.password
    )


@router.post("/token", include_in_schema=False)
async def form_data_login(
        db_session: Annotated[Session, Depends(get_db_session)],
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    return authenticate_user(
        db_session,
        email=form_data.username,
        password=form_data.password
    )


@router.delete("/logout")
async def logout(
        db_session: Annotated[Session, Depends(get_db_session)],
        user_session: Annotated[UserSession, Depends(get_current_user_session)],
):
    db_session.delete(user_session)
    db_session.commit()


@router.get("/me")
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_user)]
) -> User:
    return current_user


@router.put("/me")
async def update_users_me(
        db_session: Annotated[Session, Depends(get_db_session)],
        current_user: Annotated[User, Depends(get_current_user)],
        email: Annotated[str, Depends(get_verified_email)],
        name: Annotated[str, Body()]
) -> User:
    current_user.email = email
    current_user.name = name
    db_session.add(current_user)
    db_session.commit()

    db_session.refresh(current_user)
    return current_user


@router.put("/me/password")
async def update_my_password(
        db_session: Annotated[Session, Depends(get_db_session)],
        current_user: Annotated[User, Depends(get_current_user)],
        old_password: Annotated[str, Body()],
        new_password: Annotated[str, Depends(get_validated_password)],
) -> User:
    if not verify_password(old_password, current_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid password")
    current_user.password_hash = hash_password(new_password)
    db_session.add(current_user)
    db_session.commit()

    db_session.refresh(current_user)
    return current_user


@router.put("/{user_id}")
async def update_user_role(
        db_session: Annotated[Session, Depends(get_db_session)],
        user_id: UUID,
        roles: Annotated[list[Role], Body()]
) -> User:
    user = db_session.get(UserInDB, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.roles = roles
    db_session.add(user)
    db_session.commit()

    db_session.refresh(user)
    return user
