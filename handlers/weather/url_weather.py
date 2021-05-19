import psycopg2
import requests
from aiogram import types
from config import APPID


def url_weather():
    con = psycopg2.connect(
        database="Weathergetabot",
        user="postgres",
        password="gh5Tr43a",
        host="127.0.0.1",
        port="5432"
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
