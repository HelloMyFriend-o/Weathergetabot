import logging
import psycopg2
from aiogram import types
from loader import dp


@dp.message_handler(commands=['city'])
async def city_info(message: types.Message):

    con = psycopg2.connect(
        database="Weathergetabot",
        user="postgres",
        password="gh5Tr43a",
        host="127.0.0.1",
        port="5432"
    )
    cur = con.cursor()

    user = types.User.get_current()
    user_id = user.id

    try:
        cur.execute("SELECT city FROM users WHERE user_id = %s", (user_id,))
        city_tuple = cur.fetchone()
        city = ''.join(map(str, city_tuple))

        await message.answer(f"Выбран город:  {city}")
    except Exception:
        await message.answer("Город не указан.\n"
                             "Напишите интересующий Вас город.\n\n"
                             "Например:\n"
                             "город Казань\n"
                             "город Санкт-Петербург\n"
                             "город Нижний Новгород"
                             )

    con.commit()
    con.close()
    logging.basicConfig(level=logging.INFO)
