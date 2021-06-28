import requests
from aiogram import types

from loader import APPID
from database.db import connect_to_db


# Returns weather data in json format.
def get_weather_data():
    connection = connect_to_db()
    cursor = connection.cursor()

    # Getting data about the user who wrote the message.
    user = types.User.get_current()
    # Selecting user's latitude and longitude by his id, and assign them in variables.
    cursor.execute("SELECT lat FROM users WHERE user_id = %s", (user.id,))
    lat_tuple = cursor.fetchone()
    cursor.execute("SELECT lon FROM users WHERE user_id = %s", (user.id,))
    lon_tuple = cursor.fetchone()

    # Disconnecting from the DB.
    connection.commit()
    connection.close()
    # tuple -> float.
    lat = float(''.join(map(str, lat_tuple)))
    lon = float(''.join(map(str, lon_tuple)))
    # Indicating data which is not needed.
    exclude = 'minutely,alerts'
    # Language indication.
    lang = 'ru'
    # Specifying Units of Measure.
    units = 'metric'

    weather_request = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?"
                                   f"lat={lat}&lon={lon}&exclude={exclude}&lang={lang}&units={units}&appid={APPID}")
    return weather_request.json()
