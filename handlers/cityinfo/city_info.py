import logging
from aiogram import types
from database.db import connect_db
from handlers.weather.config import unspecified_city
from loader import dp


# Срабатывает при вводе команды "/city"
@dp.message_handler(commands=["city"])
async def city_info(message: types.Message):
    # Подключаемся к БД
    con = connect_db()
    cur = con.cursor()
    # Получаем данные о пользователе, который написал сообщение (id)
    user = types.User.get_current()
    user_id = user.id

    try:
        # Выбираем город пользователя по его id
        cur.execute("SELECT city FROM users WHERE user_id = %s", (user_id,))
        city_tuple = cur.fetchone()
        city = "".join(map(str, city_tuple))
    except TypeError:
        # Выводим это сообщение если такой пользователь не будет найден или не будет указан город
        await message.answer(unspecified_city)
    else:
        await message.answer(f"Выбран город:  {city}")
    # Отключаемся от БД
    con.commit()
    con.close()
    logging.basicConfig(level=logging.INFO)
