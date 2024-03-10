import datetime
import os
import random

import uvicorn
from sqlmodel import Session
from faker import Faker

from backend.constants import SQLITE_DB_FILE
from backend.database import create_db_and_tables, db_engine
from backend.models.confirm_receipt_request import ConfirmReceiptRequest
from backend.models.order import Order, OrderStatus
from backend.models.room import Room
from backend.models.user import UserInDB, Role
from backend.tools.user import hash_password


def gen_fake_users(session: Session, fake: Faker, multiplier=1):
    users = []
    password_hash = hash_password('P@ssw0rd')

    admin = UserInDB(
        name=fake.name(),
        email='admin@hits.ru',
        password_hash=password_hash,
    )
    admin.roles = {Role.ADMIN}
    session.add(admin)

    for _ in range(100 * multiplier):
        user = UserInDB(
            name=fake.name(),
            email=fake.email(domain="mail.ru"),
            password_hash=password_hash,
        )
        user.roles = set(random.choices(
            [
                Role.ADMIN, Role.DEAN, Role.TEACHER, Role.STUDENT,
            ], k=2)
        )
        users.append(user)
        session.add(user)
    session.commit()

    return users


def gen_fake_rooms(session: Session, fake: Faker, multiplier=1):
    rooms = []

    for _ in range(10 * multiplier):
        room = Room(
            name=fake.numerify('### (%)'),
            blocked=fake.boolean(chance_of_getting_true=10)
        )
        rooms.append(room)
        session.add(room)
    session.commit()

    return rooms


def get_start_end_datetime(fake, default_datetime):
    if fake.boolean():
        start_datetime = default_datetime + datetime.timedelta(
            days=fake.random_int(min=0, max=5),
            hours=fake.random_int(min=0, max=12),
        )
    else:
        start_datetime = default_datetime - datetime.timedelta(
            days=fake.random_int(min=0, max=14),
            hours=fake.random_int(min=0, max=12),
        )
    end_datetime = start_datetime + datetime.timedelta(minutes=90)
    return start_datetime, end_datetime


def gen_fake_data(multiplier=1):
    fake = Faker('ru_RU')

    with Session(db_engine) as session:
        users = gen_fake_users(session, fake, multiplier)
        rooms = gen_fake_rooms(session, fake, multiplier)

        now = datetime.datetime.now()
        for user in users:
            orders = []
            default_datetime = now.replace(hour=20, minute=0, second=0)
            for _ in range(fake.random_int(min=0, max=5)):
                start_datetime, end_datetime = get_start_end_datetime(fake, default_datetime)
                is_cyclic = fake.boolean(chance_of_getting_true=30)
                room = random.choice(rooms)
                order = Order(
                    user_id=user.user_id,
                    room_id=room.room_id,
                    status=random.choice([
                        OrderStatus.OPENED,
                        OrderStatus.APPROVED,
                        OrderStatus.CLOSED
                    ]),
                    cyclic=is_cyclic,
                    day=None if is_cyclic else start_datetime.date(),
                    week_day=random.randint(0, 5) if is_cyclic else None,
                    start_time=start_datetime.time(),
                    end_time=end_datetime.time()
                )
                if order.status == OrderStatus.APPROVED and start_datetime < now < end_datetime:
                    request = ConfirmReceiptRequest(
                        user_id=user.user_id,
                        room_id=room.room_id,
                        deadline=end_datetime
                    )
                    session.add(request)

                orders.append(order)
                session.add(order)
            session.commit()


if __name__ == "__main__":
    if not os.path.exists(SQLITE_DB_FILE):
        print("Creating database...")
        create_db_and_tables()
        print("Database created!")
        print("Generating fake data...")
        gen_fake_data(multiplier=1)
        print("Fake data generated!")

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
