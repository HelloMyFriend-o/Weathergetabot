from aiogram import types

from database.db import connect_to_db
from handlers.weather.config import unspecified_city
from loader import dp


# Triggered when user enter the command "/city".
@dp.message_handler(commands=["city"])
async def get_city_info(message: types.Message):
    connection = connect_to_db()
    cursor = connection.cursor()
    # Getting data about the user who wrote the message.
    user = types.User.get_current()
    user_id = user.id

    try:
        # Selecting user's city by his id.
        cursor.execute("SELECT city FROM users WHERE user_id = %s", (user_id,))
        city_tuple = cursor.fetchone()
        city = "".join(map(str, city_tuple))
    except TypeError:
        # Send this message if such user is not found or city is not specified.
        await message.answer(unspecified_city)
    else:
        await message.answer(f"Выбран город:  {city}")
    # Disconnecting from the DB.
    connection.commit()
    connection.close()
