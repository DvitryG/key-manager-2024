import os
import uvicorn
from backend.main import create_db_and_tables


if __name__ == "__main__":
    if not os.path.exists(os.getenv("SQLITE_DB_FILE")):
        create_db_and_tables()

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
