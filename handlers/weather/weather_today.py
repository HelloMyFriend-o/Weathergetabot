from aiogram import types

import keyboards as kb
from loader import dp
from .config import *
from .get_weather_data import get_weather_data


# Срабатывает когда пользователь нажимает на кнопку "Текущая погода" (или оправляет эту фразу сам)
@dp.message_handler(text=["Текущая погода"])
async def weather_today(message: types.Message):
    try:
        # Пробуем получить данные о погоде
        data = get_weather_data()
    except TypeError:
        # Выводим это сообщение, если пользователь запрашивает погоду до того, как указал город
        await message.answer(unspecified_city)
    else:
        # Иначе выводим данные о погоде
        today = data["daily"][0]["temp"]
        await message.answer(f'Сейчас: {sign(data["current"]["temp"])}{round(data["current"]["temp"])} {degree}\n'
                             f'Ощущается как: {sign(data["current"]["feels_like"])}{round(data["current"]["feels_like"])} {degree}\n\n'
                             f'Утром: {sign(today["morn"])}{round(today["morn"])} {degree}\n'
                             f'Днём: {sign(today["morn"])}{round(today["day"])} {degree}\n'
                             f'Вечером: {sign(today["eve"])}{round(today["eve"])} {degree}\n'
                             f'Ночью: {sign(today["night"])}{round(today["night"])} {degree}\n\n'
                             f'Ветер: {round(data["current"]["wind_speed"])} м/с\n'
                             f'{data["current"]["weather"][0]["description"].capitalize()}\n')
        # Выводим смайлик погоды и кпопку "Подробнее"
        await message.answer(f'{weather_icons[data["current"]["weather"][0]["icon"]]}', reply_markup=kb.detailed_today)
