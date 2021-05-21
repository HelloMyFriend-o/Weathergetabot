import datetime
from aiogram.types import CallbackQuery
from loader import dp
from ..config import *
from ..url_weather import url_weather


@dp.callback_query_handler(text="detailed_tomorrow")
async def detailed_weather_tomorrow(call: CallbackQuery):
    try:
        data = url_weather()
    except TypeError:
        pass
    else:
        detailed_message = f'{datetime.datetime.fromtimestamp(data["daily"][1]["dt"]).strftime("%a: %d.%m")}\n\n' \
                           f'Давление: {round(data["daily"][0]["pressure"] * hpa_to_mmhg)} мм рт.ст.\n' \
                           f'Влажность: {data["daily"][0]["humidity"]} % \n\n'
        count = 0
        toggle = False
        for hour in data['hourly']:
            time = datetime.datetime.fromtimestamp(hour["dt"]).strftime('%H:%M')
            temp = round(hour["temp"])
            description = hour["weather"][0]["description"]
            icon = hour["weather"][0]["icon"]

            if (time == '00:00' or toggle) and count < 24:
                detailed_message += f'{time}  {sign(temp)}{temp} {degree}, {description}{weather_icons[icon]} \n'
                count += 1
                toggle = True
        await call.message.answer(detailed_message)
