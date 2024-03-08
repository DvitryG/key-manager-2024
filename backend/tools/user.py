from datetime import timedelta, datetime, timezone
from difflib import SequenceMatcher
from itertools import product

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from sqlmodel import Session, select
from starlette import status

from backend.constants import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from backend.models.user import (
    Token,
    UserInDB,
    UserSession
)
from backend.tools.common import FiltersCache

_pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(db_session: Session, email: str, password: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = db_session.exec(
        select(UserInDB).where(UserInDB.email == email)
    ).first()

    if not user:
        raise credentials_exception
    if not _pwd_context.verify(password, user.password_hash):
        raise credentials_exception

    user_session = UserSession(user_id=user.user_id)
    db_session.add(user_session)
    db_session.commit()

    access_token = create_access_token(
        data={"sub": user_session.session_id.hex},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return Token(access_token=access_token, token_type="bearer")


def hash_password(password: str):
    return _pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return _pwd_context.verify(plain_password, hashed_password)


def is_similar_usernames(user_name: str, search_name: str) -> bool:
    user_words = user_name.split()
    search_words = search_name.strip().split()

    if len(search_words) > len(user_words):
        return False

    matches = sorted(map(
        lambda words: SequenceMatcher(None, words[0], words[1]).ratio(),
        product(user_words, search_words),
    ), reverse=True)[:len(search_words)]

    return sum(matches) / len(matches) > 0.7


class UserFiltersCache(FiltersCache):
    pass
