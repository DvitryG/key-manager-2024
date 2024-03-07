from sqlmodel import SQLModel, create_engine
from backend.constants import DATABASE_URL
import backend.models


db_engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(db_engine)
