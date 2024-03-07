from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, Body
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from password_validator import PasswordValidator
from sqlmodel import Session, select
from starlette import status
from email_validator import validate_email, EmailNotValidError

from backend.constants import SECRET_KEY, ALGORITHM
from backend.dependencies.database import get_db_session
from backend.models.user import UserInDB, UserSession

oauth2_scheme = OAuth2PasswordBearer('users/token')


def get_current_user_and_session(
        db_session: Annotated[Session, Depends(get_db_session)],
        token: Annotated[str, Depends(oauth2_scheme)]
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        session_id = payload.get("sub") and UUID(payload.get("sub"))
        if session_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user_session = db_session.get(UserSession, session_id)
    if user_session is None:
        raise credentials_exception

    user = db_session.get(UserInDB, user_session.user_id)
    if user is None:
        raise credentials_exception

    return {'user': user, 'session': user_session}


def get_current_user(
        user_and_session: Annotated[dict, Depends(get_current_user_and_session)],
) -> UserInDB:
    return user_and_session['user']


def get_current_user_session(
        user_and_session: Annotated[dict, Depends(get_current_user_and_session)],
) -> UserSession:
    return user_and_session['session']


def get_verified_email(
        db_session: Annotated[Session, Depends(get_db_session)],
        email: Annotated[str, Body()],
):
    try:
        email_object = validate_email(email)
    except EmailNotValidError as e:
        raise HTTPException(status_code=400, detail=str(e))

    user = db_session.exec(
        select(UserInDB).where(UserInDB.email == email_object.normalized)
    ).first()

    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return email_object.normalized


_password_schema = PasswordValidator()

_password_schema\
    .min(8)\
    .max(64)\
    .has().uppercase()\
    .has().lowercase()\
    .has().digits()\
    .has().symbols()


def get_validated_password(
        password: Annotated[str, Body(min_length=8)]
):
    if not _password_schema.validate(password):
        raise HTTPException(
            status_code=400,
            detail="password requirements: 8-64 characters long, upper and lower case, numbers, symbols"
        )
    return password
