import os
from dotenv import load_dotenv

load_dotenv('.env')

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
SQLITE_DB_FILE = os.getenv("SQLITE_DB_FILE")
DATABASE_URL = os.getenv("DATABASE_URL")

FILTER_BATCH_SIZE = int(os.getenv("FILTER_BATCH_SIZE"))
