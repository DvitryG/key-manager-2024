import os
import time
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine
from backend import models
from backend.routers import (
    user,
    room,
    order,
    obligation,
    confirm_return_request,
    confirm_receipt_request
)

load_dotenv('.env')
app = FastAPI()
db_engine = create_engine(os.getenv("DATABASE_URL"), echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(db_engine)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(user.router)
app.include_router(room.router)
app.include_router(order.router)
app.include_router(obligation.router)
app.include_router(confirm_return_request.router)
app.include_router(confirm_receipt_request.router)
