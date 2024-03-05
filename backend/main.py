import time
from fastapi import FastAPI, Request
from dotenv import load_dotenv

from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

from backend.routers import (
    user,
    room,
    order,
    obligation,
    confirm_return_request,
    confirm_receipt_request
)

from backend.models.user import (
    User
)

load_dotenv('.env')
app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

#app.include_router(user.router)
app.include_router(room.router)
app.include_router(order.router)
app.include_router(obligation.router)
app.include_router(confirm_return_request.router)
app.include_router(confirm_receipt_request.router)


def create_db_and_tables(engine1):
    SQLModel.metadata.create_all(engine1)


#if __name__ == "__main__":
#engine = db.setup_engine()
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)
create_db_and_tables(engine)

