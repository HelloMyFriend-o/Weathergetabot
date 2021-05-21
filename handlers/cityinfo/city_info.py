import logging
from aiogram import types
from database.db import connect_db
from handlers.weather.config import unspecified_city
from loader import dp


@dp.message_handler(commands=["city"])
async def city_info(message: types.Message):
    con = connect_db()
    cur = con.cursor()

    user = types.User.get_current()
    user_id = user.id

    try:
        cur.execute("SELECT city FROM users WHERE user_id = %s", (user_id,))
        city_tuple = cur.fetchone()
        city = "".join(map(str, city_tuple))
    except TypeError:
        await message.answer(unspecified_city)
    else:
        await message.answer(f"Выбран город:  {city}")

    con.commit()
    con.close()
    logging.basicConfig(level=logging.INFO)
