import psycopg2 as psycopg2

from loader import PG_DB, PG_USER, PG_PASS, PG_HOST, PG_PORT


def connect_db():
    con = psycopg2.connect(
        database=PG_DB,
        user=PG_USER,
        password=PG_PASS,
        host=PG_HOST,
        port=PG_PORT
    )
    return con


def create_tb():
    con = connect_db()

    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users
    (
        first_name TEXT,
        last_name TEXT,
        user_id INTEGER,
        city TEXT,
        lat FLOAT,
        lon FLOAT
    )""")

    # Disconnecting from the DB.
    con.commit()
    con.close()
