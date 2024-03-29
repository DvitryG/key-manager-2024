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
    get_current_user_session,
    authorize
)
from backend.models.common import Pagination
from backend.models.user import (
    User,
    Token,
    UserInDB,
    LoginRequest,
    Role,
    UserSession, UsersPageResponse, UserResponse
)
from backend.tools.common import (
    get_filtered_items,
    get_filtered_count,
    get_pages_count_from_cache
)
from backend.tools.user import (
    hash_password,
    authenticate_user,
    verify_password,
    is_similar_usernames, UserFiltersCache
)

router = APIRouter(
    prefix="/users",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", dependencies=[Depends(
    authorize(Role.ADMIN, Role.DEAN)
)])
async def get_all_users(
        db_session: Annotated[Session, Depends(get_db_session)],
        name: Annotated[str | None, Query()] = None,
        page: Annotated[int, Query(ge=0)] = 0,
        page_size: Annotated[int, Query(ge=1, le=100)] = 10
) -> UsersPageResponse:
    result = await get_filtered_items(
        db_session, UserInDB, lambda user_in_db: is_similar_usernames(user_in_db.name, name),
        offset=page * page_size, limit=page_size
    ) if name else db_session.exec(
        select(UserInDB).offset(page * page_size).limit(page_size)
    ).all()

    users = []
    for user in result:
        users.append(UserResponse(
            **user.model_dump(exclude={'password_hash', 'roles_str'}),
            roles=user.roles
        ))

    pages_count = await get_pages_count_from_cache(
        lambda: get_filtered_count(
            db_session, UserInDB, lambda user_in_db: is_similar_usernames(user.name, name)
        ) if name else db_session.query(UserInDB).count(),
        UserFiltersCache,
        {"name": name, "page_size": page_size}
    )

    return UsersPageResponse(
        users=users,
        pagination=Pagination(
            page_size=len(users),
            pages_count=pages_count,
            current_page=page,
        )
    )


@router.get("/search", dependencies=[Depends(authorize())])
async def search_users(
        db_session: Annotated[Session, Depends(get_db_session)],
        name: Annotated[str, Query()],
        limit: Annotated[int, Query(ge=1, le=100)],
) -> Sequence[UserResponse]:
    if not name:
        return []

    result = await get_filtered_items(
        db_session, UserInDB,
        lambda user_in_db: is_similar_usernames(user_in_db.name, name),
        limit=limit
    )

    users = []
    for user in result:
        users.append(UserResponse(
            **user.model_dump(exclude={'password_hash', 'roles_str'}),
            roles=user.roles
        ))

    return users


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
    UserFiltersCache.clear()

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
) -> UserResponse:
    return UserResponse(
        **current_user.model_dump(exclude={'password_hash', 'roles_str'}),
        roles=current_user.roles
    )


@router.put("/me")
async def update_users_me(
        db_session: Annotated[Session, Depends(get_db_session)],
        current_user: Annotated[User, Depends(get_current_user)],
        email: Annotated[str, Depends(get_verified_email)],
        name: Annotated[str, Body()]
) -> UserResponse:
    current_user.email = email
    current_user.name = name
    db_session.add(current_user)
    db_session.commit()
    UserFiltersCache.clear()

    db_session.refresh(current_user)
    return UserResponse(
        **current_user.model_dump(exclude={'password_hash', 'roles_str'}),
        roles=current_user.roles
    )


@router.put("/me/password")
async def update_my_password(
        db_session: Annotated[Session, Depends(get_db_session)],
        current_user: Annotated[User, Depends(get_current_user)],
        old_password: Annotated[str, Body()],
        new_password: Annotated[str, Depends(get_validated_password)],
) -> UserResponse:
    if not verify_password(old_password, current_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid password")
    current_user.password_hash = hash_password(new_password)
    db_session.add(current_user)
    db_session.commit()

    db_session.refresh(current_user)
    return UserResponse(
        **current_user.model_dump(exclude={'password_hash', 'roles_str'}),
        roles=current_user.roles
    )


@router.put("/{user_id}")
async def update_user_role(
        db_session: Annotated[Session, Depends(get_db_session)],
        user_id: UUID,
        include: Annotated[set[Role], Body()],
        exclude: Annotated[set[Role], Body()],
        current_user_roles: Annotated[set[Role], Depends(
            authorize(Role.ADMIN, Role.DEAN)
        )],
) -> UserResponse:
    permission_error = HTTPException(
        status_code=403,
        detail="Not enough permissions"
    )
    include_or_exclude = include | exclude

    if include & exclude:
        raise HTTPException(
            status_code=400,
            detail="Cannot include and exclude the same roles"
        )

    if Role.ADMIN in include_or_exclude:
        raise permission_error

    if Role.DEAN in include_or_exclude and Role.ADMIN not in current_user_roles:
        raise permission_error

    target_user = db_session.get(UserInDB, user_id)
    if not target_user:
        raise HTTPException(status_code=404, detail="User not found")

    target_user.roles = target_user.roles - exclude | include

    db_session.add(target_user)
    db_session.commit()
    UserFiltersCache.clear()

    db_session.refresh(target_user)
    return UserResponse(
        **target_user.model_dump(exclude={'password_hash', 'roles_str'}),
        roles=target_user.roles
    )
