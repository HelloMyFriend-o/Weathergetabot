import psycopg2 as psycopg2

from loader import PG_DB, PG_USER, PG_PASS, PG_HOST, PG_PORT


def connect_to_db():
    connection = psycopg2.connect(
        database=PG_DB,
        user=PG_USER,
        password=PG_PASS,
        host=PG_HOST,
        port=PG_PORT
    )
    return connection


def create_a_tb():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users
    (
        first_name TEXT,
        last_name TEXT,
        user_id INTEGER,
        city TEXT,
        lat FLOAT,
        lon FLOAT
    )""")

    # Disconnecting from the DB.
    connection.commit()
    connection.close()
