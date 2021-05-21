import requests
from aiogram import types
from config import APPID
from database.db import connect_db


def url_weather():
    con = connect_db()
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
