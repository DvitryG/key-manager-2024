import os
import uvicorn
from backend.constants import SQLITE_DB_FILE
from backend.database import create_db_and_tables


if __name__ == "__main__":
    if not os.path.exists(SQLITE_DB_FILE):
        print("Creating database...")
        create_db_and_tables()
        print("Database created!")

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
