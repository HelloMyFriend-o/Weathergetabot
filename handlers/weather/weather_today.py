from aiogram import types

import keyboards as kb
from loader import dp
from .config import *
from .get_weather_data import get_weather_data


# Triggered when user clicks on the "Текущая погода" button (or sends this phrase by himself).
@dp.message_handler(text=["Текущая погода"])
async def weather_today(message: types.Message):
    try:
        # Trying to get the weather data.
        data = get_weather_data()
    except TypeError:
        # Send this message if user asks for the weather before specifying a city.
        await message.answer(unspecified_city)
    else:
        # Otherwise, send the weather data.
        today = data["daily"][0]["temp"]
        await message.answer(f'Сейчас: {sign(data["current"]["temp"])}{round(data["current"]["temp"])} {degree}\n'
                             f'Ощущается как: {sign(data["current"]["feels_like"])}{round(data["current"]["feels_like"])} {degree}\n\n'
                             f'Утром: {sign(today["morn"])}{round(today["morn"])} {degree}\n'
                             f'Днём: {sign(today["morn"])}{round(today["day"])} {degree}\n'
                             f'Вечером: {sign(today["eve"])}{round(today["eve"])} {degree}\n'
                             f'Ночью: {sign(today["night"])}{round(today["night"])} {degree}\n\n'
                             f'Ветер: {round(data["current"]["wind_speed"])} м/с\n'
                             f'{data["current"]["weather"][0]["description"].capitalize()}\n')
        # Send the weather emoticon and the "Подробнее" button.
        await message.answer(f'{weather_icons[data["current"]["weather"][0]["icon"]]}', reply_markup=kb.detailed_today)
