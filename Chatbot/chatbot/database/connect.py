import os
import mysql.connector

_DATABASE_ = os.getenv("_DATABASE_")

def set_connecttiom():
    conn = mysql.connector.connect(
        host=_DATABASE_["host"],
        user=_DATABASE_["user_name"],
        password=_DATABASE_["password"],
        database=_DATABASE_["database_name"]
    )
    return conn