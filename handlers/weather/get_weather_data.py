import requests
from aiogram import types

from loader import APPID
from database.db import connect_db


# Returns weather data in json format.
def get_weather_data():
    # Connecting to the DB.
    con = connect_db()
    cur = con.cursor()

    # Getting data about the user who wrote the message.
    user = types.User.get_current()
    # Selecting the user's latitude and longitude by its id, and assign them in variables.
    cur.execute("SELECT lat FROM users WHERE user_id = %s", (user.id,))
    lat_tuple = cur.fetchone()
    cur.execute("SELECT lon FROM users WHERE user_id = %s", (user.id,))
    lon_tuple = cur.fetchone()

    # Disconnecting from the DB.
    con.commit()
    con.close()
    # tuple -> float.
    lat = float(''.join(map(str, lat_tuple)))
    lon = float(''.join(map(str, lon_tuple)))
    # Indicating what data is not needed.
    exclude = 'minutely,alerts'
    # Language indication.
    lang = 'ru'
    # Specifying Units of Measure.
    units = 'metric'

    weather_request = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?"
                                   f"lat={lat}&lon={lon}&exclude={exclude}&lang={lang}&units={units}&appid={APPID}")
    return weather_request.json()
