import logging
import requests
import keyboards as kb
from aiogram import types
from config import APPID
from database.db import connect_db
from loader import dp


@dp.message_handler(lambda msg: msg["text"].lower().split(" ")[0] == "город")
async def city_change(message: types.Message):
    city_in_msg = " ".join(message["text"].split(" ")[1:]).title()
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_in_msg}&appid={APPID}")
    data = r.json()

    con = connect_db()
    cur = con.cursor()

    user = types.User.get_current()
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name

    cur.execute("SELECT user_id FROM users WHERE user_id = %s", (user_id,))
    if cur.fetchall():
        try:
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
            await message.answer("Некорректное название города")
        else:
            await message.answer("Город обновлен", reply_markup=kb.weather_kb)
    else:
        try:
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
            await message.answer("Некорректное название города")
        else:
            await message.answer("Город обновлен", reply_markup=kb.weather_kb)

    con.commit()
    con.close()
    logging.basicConfig(level=logging.INFO)
