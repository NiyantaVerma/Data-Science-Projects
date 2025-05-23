import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
_DATABASE_ = os.getenv("_DATABASE_")

def read(conn, sessionId: str) -> str:
    # query = "SELECT SessionID FROM Coustomer_convo WHERE SessionID = %s;"
    # cursor = conn.cursor()
    # cursor.execute(query, (sessionId,))
    # result = cursor.fetchone()
    # cursor.close()
    # return result
    return {
        sessionId: "123456789"
    }

def create() -> None:
    # Insert new rows
    return

def update() -> None:
    # updating or inserting into db
    return

def delete() -> str:
    # deleting an entry in db
    return