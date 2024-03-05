from sqlmodel import Field, SQLModel, create_engine


def setup_engine():
    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine = create_engine(sqlite_url, echo=True)
    return engine

