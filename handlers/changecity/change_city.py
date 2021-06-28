import requests

from aiogram.dispatcher import filters
from aiogram import types

import keyboards as kb
from loader import dp, APPID
from database.db import connect_to_db


# Triggered when user sends a message that starts with the word "город".
@dp.message_handler(filters.Text(startswith='город', ignore_case=True))
async def change_city(message: types.Message):
    # Words from the text of the message sent by user are separated by space and added to the list.
    # Words, from the list, are concatenated back into a string without the first word (город).
    city_in_msg = " ".join(message["text"].split(" ")[1:]).title()

    # Getting weather data of the city that was written in the message.
    # Used it only to get the latitude and longitude of the specified city, and store them in the table by user id.
    # This data is necessary, because a latitude and longitude query gives more weather data than a city name query.
    weather_request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_in_msg}&appid={APPID}")
    data = weather_request.json()

    connection = connect_to_db()
    cursor = connection.cursor()
    # Getting data about the user who wrote the message.
    user = types.User.get_current()
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    # Selecting the user who wrote the message by his id in the DB.
    cursor.execute("SELECT user_id FROM users WHERE user_id = %s", (user_id,))
    # Checking is it in the DB.
    if cursor.fetchall():
        try:
            # If it is, and the name of the city was specified correctly,
            # then it updates the city, latitude and longitude.
            cursor.execute(
                "UPDATE users SET city = %s, lat = %s, lon = %s WHERE user_id = %s",
                (
                    city_in_msg,
                    data["coord"]["lat"],
                    data["coord"]["lon"],
                    user_id
                )
            )
        except KeyError:
            # If a city was specified incorrectly, displays a message in the chat about it.
            await message.answer("Некорректное название города")
        else:
            # If a city was specified correctly, displays a message in the chat about it and updates the buttons.
            await message.answer("Город обновлен", reply_markup=kb.weather_keyboard)
    else:
        try:
            # If it's not, and the name of the city was specified correctly,
            # then add first name, last name, id, city, latitude and longitude.
            cursor.execute(
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
            # If a city was specified incorrectly, displays a message in the chat about it.
            await message.answer("Некорректное название города")
        else:
            # If a city was specified correctly, displays a message in the chat about it and updates the buttons.
            await message.answer("Город обновлен", reply_markup=kb.weather_keyboard)
    # Disconnecting from the DB.
    connection.commit()
    connection.close()
