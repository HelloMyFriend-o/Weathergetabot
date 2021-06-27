import requests

from aiogram.dispatcher import filters
from aiogram import types

import keyboards as kb
from loader import dp, APPID
from database.db import connect_db


# Triggered when user sends a message that starts with the word "город".
@dp.message_handler(filters.Text(startswith='город', ignore_case=True))
async def city_change(message: types.Message):
    # Words from the text of the message sent by user are separated by space and added to the list.
    # From the list, words are concatenated back into a string without the first word (город).
    city_in_msg = " ".join(message["text"].split(" ")[1:]).title()

    # Getting data on weather in the city that was indicated in the message.
    # Used it only to get the latitude and longitude of the specified city, and store them in the table by user id.
    # This data is needed, because a latitude and longitude query gives more weather data than a city name query.
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_in_msg}&appid={APPID}")
    data = r.json()
    # Connecting to the DB.
    con = connect_db()
    cur = con.cursor()
    # Getting data about user who wrote the message.
    user = types.User.get_current()
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    # Selecting user who wrote the message by his id in the DB.
    cur.execute("SELECT user_id FROM users WHERE user_id = %s", (user_id,))
    # Checking if it is in the DB.
    if cur.fetchall():
        try:
            # If there is, and the name of the city was specified correctly,
            # then it updates the city, latitude and longitude.
            cur.execute(
                "UPDATE users SET city = %s, lat = %s, lon = %s WHERE user_id = %s",
                (
                    city_in_msg,
                    data["coord"]["lat"],
                    data["coord"]["lon"],
                    user_id
                )
            )
        except KeyError:
            # If city was specified incorrectly, displays a message in the chat about it.
            await message.answer("Некорректное название города")
        else:
            # If city was specified correctly, displays a message in the chat about it and updates the buttons.
            await message.answer("Город обновлен", reply_markup=kb.weather_kb)
    else:
        try:
            # If not, and the name of city was specified correctly,
            # then add first name, last name, id, city, latitude and longitude.
            cur.execute(
                "INSERT INTO users (first_name, last_name, user_id, city, lat, lon)"
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    first_name,
                    last_name,
                    user_id,
                    city_in_msg,
                    data["coord"]["lat"],
                    data["coord"]["lon"]
                )
            )
        except KeyError:
            # If city was specified incorrectly, displays a message in the chat about it.
            await message.answer("Некорректное название города")
        else:
            # If city was specified correctly, displays a message in the chat about it and updates the buttons.
            await message.answer("Город обновлен", reply_markup=kb.weather_kb)
    # Disconnecting from the DB.
    con.commit()
    con.close()
