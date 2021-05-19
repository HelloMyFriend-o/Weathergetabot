import datetime
from aiogram.types import CallbackQuery
from loader import dp
from ..config import *
from ..url_weather import url_weather


@dp.callback_query_handler(text="detailed_today")
async def detailed_weather_today(call: CallbackQuery):
    data = url_weather()
    detailed_message = f'Давление: {round(data["daily"][0]["pressure"]*hpa_to_mmhg)} мм рт.ст.\n' \
                       f'Влажность: {data["daily"][0]["humidity"]} % \n\n'
    for hour in data['hourly'][:-24]:
        time = datetime.datetime.fromtimestamp(hour["dt"]).strftime('%H:%M')
        temp = round(hour["temp"])
        description = hour["weather"][0]["description"]
        icon = hour["weather"][0]["icon"]
        detailed_message += f'{time}  {sign(temp)}{temp} {degree}, {description}{weather_icons[icon]} \n'
    await call.message.answer(detailed_message)
