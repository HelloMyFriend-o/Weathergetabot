import psycopg2
import requests
from aiogram import types
from config import APPID, PG_DB, PG_USER, PG_PASS, PG_HOST, PG_PORT


def url_weather():
    con = psycopg2.connect(
        database=PG_DB,
        user=PG_USER,
        password=PG_PASS,
        host=PG_HOST,
        port=PG_PORT
    )
    cur = con.cursor()

    user = types.User.get_current()

    cur.execute("SELECT lat FROM users WHERE user_id = %s", (user.id,))
    lat_tuple = cur.fetchone()

    cur.execute("SELECT lon FROM users WHERE user_id = %s", (user.id,))
    lon_tuple = cur.fetchone()

    con.commit()
    con.close()

    lat = float(''.join(map(str, lat_tuple)))
    lon = float(''.join(map(str, lon_tuple)))

    exclude = 'minutely,alerts'
    lang = 'ru'
    units = 'metric'

    r = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?"
                     f"lat={lat}&lon={lon}&exclude={exclude}&lang={lang}&units={units}&appid={APPID}")
    return r.json()
