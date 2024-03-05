from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

class SimpleOrder(BaseModel):
    order_id: int
    user_id: int
    room_number: int
    date: date
    start_time: str
    return_time: str
    status: str


class CyclicOrder(SimpleOrder):
    is_cyclic: bool = False    


class Pagination(BaseModel):
    size: int
    count: int 
    current: int 
