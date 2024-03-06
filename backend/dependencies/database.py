from backend.main import db_engine
from sqlmodel import Session


def get_db_session():
    session = Session(db_engine)
    try:
        yield session
    finally:
        session.close()
