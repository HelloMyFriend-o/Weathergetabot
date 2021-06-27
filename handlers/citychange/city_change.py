import requests

from aiogram.dispatcher import filters
from aiogram import types

import keyboards as kb
from loader import dp, APPID
from database.db import connect_db


# Срабатывает когда пользователь отправляет сообщение, которое начинается со слова "город"
@dp.message_handler(filters.Text(startswith='город', ignore_case=True))
async def city_change(message: types.Message):
    # Слова из текста сообщения, отправленного пользователем, разделяются по пробелу и добавляются в список
    # Из списка слова объединяются обратно в строку без первого слова (город)
    city_in_msg = " ".join(message["text"].split(" ")[1:]).title()

    # Получаем данные о погоде в городе, который был указан в сообщении.
    # Используем только для того, чтобы получить долготу и широту указанного города, и сохранить их в таблице
    # по id пользователя.
    # Эти данные нам нужны, т.к. запрос по долготе и широте дает больше данных о погоде, чем запрос по названию города
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_in_msg}&appid={APPID}")
    data = r.json()
    # Подключаемся к БД
    con = connect_db()
    cur = con.cursor()
    # Получаем данные о пользователе, который написал сообщение (id, имя, фамилию)
    user = types.User.get_current()
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    # Выбираем пользователя, написавшего сообщение, по его id в БД
    cur.execute("SELECT user_id FROM users WHERE user_id = %s", (user_id,))
    # Проверяем есть ли он в БД
    if cur.fetchall():
        try:
            # Если есть, и название города было указано корректно, то обновляет город, долготу и широту
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
            # Выводим в чат сообщение, если город был указан некорректно
            await message.answer("Некорректное название города")
        else:
            # Выводим в чат сообщение, если город был указан корректно, и обновляем кнопки
            await message.answer("Город обновлен", reply_markup=kb.weather_kb)
    else:
        try:
            # Если нет, и название города было указано корректно, то добавляем имя, фамилию, id,
            # город, долготу и широту
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
            # Выводим в чат сообщение, если город был указан некорректно
            await message.answer("Некорректное название города")
        else:
            # Выводим в чат сообщение, если город был указан корректно, и обновляет кнопки
            await message.answer("Город обновлен", reply_markup=kb.weather_kb)
    # Отключаемся от БД
    con.commit()
    con.close()
