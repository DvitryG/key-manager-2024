import os
from sqlmodel import SQLModel, create_engine
from backend import app_env
from backend import models

db_engine = create_engine(os.getenv("DATABASE_URL"), echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(db_engine)