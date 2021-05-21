import datetime
from aiogram import types
from loader import dp
from .config import *
from .url_weather import url_weather


@dp.message_handler(text=["Погода на неделю"])
async def weather_week(message: types.Message):
    try:
        data = url_weather()
    except TypeError:
        await message.answer(unspecified_city)
    else:
        for day in data["daily"]:
            await message.answer(f'{datetime.datetime.fromtimestamp(day["dt"]).strftime("%a: %d.%m")}\n\n'
                                 f'Утром: {sign(day["temp"]["morn"])}{round(day["temp"]["morn"])} {degree}\n'
                                 f'Днём: {sign(day["temp"]["day"])}{round(day["temp"]["day"])} {degree}\n'
                                 f'Вечером: {sign(day["temp"]["eve"])}{round(day["temp"]["eve"])} {degree}\n'
                                 f'Ночью: {sign(day["temp"]["night"])}{round(day["temp"]["night"])} {degree}\n\n'
                                 f'Ветер: {round(day["wind_speed"])} м/с\n'
                                 f'{day["weather"][0]["description"].capitalize()}\n')
            await message.answer(f'{weather_icons[day["weather"][0]["icon"]]}')
