import psycopg2 as psycopg2

from config import PG_DB, PG_USER, PG_PASS, PG_HOST, PG_PORT


def create_db():
    con = psycopg2.connect(
        database=PG_DB,
        user=PG_USER,
        password=PG_PASS,
        host=PG_HOST,
        port=PG_PORT
    )

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

    con.commit()
    con.close()
