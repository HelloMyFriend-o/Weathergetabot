import psycopg2 as psycopg2

from loader import PG_DB, PG_USER, PG_PASS, PG_HOST, PG_PORT


# Подключаемся к БД
def connect_db():
    con = psycopg2.connect(
        database=PG_DB,
        user=PG_USER,
        password=PG_PASS,
        host=PG_HOST,
        port=PG_PORT
    )
    return con


# Создание таблицы в которой будут
# храниться данные пользователей. А именно:
#                                           - Имя
#                                           - Фамилия
#                                           - id
#                                           - Выбранный город
#                                           - долгота выбранного города
#                                           - широта выбранного города
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

    con.commit()
    con.close()
