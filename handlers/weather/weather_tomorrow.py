import datetime

from aiogram import types

import keyboards as kb
from loader import dp
from .config import *
from .get_weather_data import get_weather_data


# Срабатывает когда пользователь нажимает на кнопку "Погода на завтра" (или оправляет эту фразу сам)
@dp.message_handler(text=["Погода на завтра"])
async def weather_tomorrow(message: types.Message):
    try:
        # Пробуем получить данные о погоде
        data = get_weather_data()
    except TypeError:
        # Выводим это сообщение, если пользователь запрашивает погоду до того, как указал город
        await message.answer(unspecified_city)
    else:
        # Иначе выводим данные о погоде и дне недели
        tomorrow_temp = data["daily"][1]["temp"]
        tomorrow_daily = data["daily"][1]
        await message.answer(f'{datetime.datetime.fromtimestamp(tomorrow_daily["dt"]).strftime("%a: %d.%m")}\n\n'
                             f'Утром: {sign(tomorrow_temp["morn"])}{round(tomorrow_temp["morn"])} {degree}\n'
                             f'Днём: {sign(tomorrow_temp["day"])}{round(tomorrow_temp["day"])} {degree}\n'
                             f'Вечером: {sign(tomorrow_temp["eve"])}{round(tomorrow_temp["eve"])} {degree}\n'
                             f'Ночью: {sign(tomorrow_temp["night"])}{round(tomorrow_temp["night"])} {degree}\n\n'
                             f'Ветер: {round(tomorrow_daily["wind_speed"])} м/с\n'
                             f'{tomorrow_daily["weather"][0]["description"].capitalize()}\n')
        # Выводим смайлик погоды и кпопку "Подробнее"
        await message.answer(f'{weather_icons[tomorrow_daily["weather"][0]["icon"]]}',
                             reply_markup=kb.detailed_tomorrow)
