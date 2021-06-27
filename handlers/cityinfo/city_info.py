from aiogram import types

from database.db import connect_db
from handlers.weather.config import unspecified_city
from loader import dp


# Triggered when you enter the command "/city".
@dp.message_handler(commands=["city"])
async def city_info(message: types.Message):
    # Connecting to the DB.
    con = connect_db()
    cur = con.cursor()
    # Getting data about user who wrote the message.
    user = types.User.get_current()
    user_id = user.id

    try:
        # Selecting user's city by its id.
        cur.execute("SELECT city FROM users WHERE user_id = %s", (user_id,))
        city_tuple = cur.fetchone()
        city = "".join(map(str, city_tuple))
    except TypeError:
        # Send this message if such user is not found or city is not specified.
        await message.answer(unspecified_city)
    else:
        await message.answer(f"Выбран город:  {city}")
    # Disconnecting from the DB.
    con.commit()
    con.close()
