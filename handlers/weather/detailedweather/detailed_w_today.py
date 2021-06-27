import datetime

from aiogram.types import CallbackQuery

from loader import dp
from ..config import *
from ..get_weather_data import get_weather_data


# Triggered when user click on "Подробнее" button after the request for "Текущая погода".
@dp.callback_query_handler(text="detailed_today")
async def detailed_weather_today(call: CallbackQuery):
    try:
        # Trying to get the weather data.
        data = get_weather_data()
    except TypeError:
        # Send this message if user asks for the weather before specifying a city.
        await call.message.answer(unspecified_city)
    else:
        detailed_message = f'Давление: {round(data["daily"][0]["pressure"] * hpa_to_mmhg)} мм рт.ст.\n' \
                           f'Влажность: {data["daily"][0]["humidity"]} % \n\n'
        # The received data shows the weather for the next 48 hours. Display only the first 24 of them.
        for hour in data['hourly'][:-24]:
            time = datetime.datetime.fromtimestamp(hour["dt"]).strftime('%H:%M')
            temp = round(hour["temp"])
            description = hour["weather"][0]["description"]
            icon = hour["weather"][0]["icon"]
            detailed_message += f'{time}  {sign(temp)}{temp} {degree}, {description}{weather_icons[icon]} \n'
        # Send a message indicating the weather by hour.
        await call.message.answer(detailed_message)
