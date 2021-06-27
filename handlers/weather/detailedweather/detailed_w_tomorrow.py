import datetime

from aiogram.types import CallbackQuery

from loader import dp
from ..config import *
from ..get_weather_data import get_weather_data


# Triggered when user click on "Подробнее" button after the request for "Погода на завтра".
@dp.callback_query_handler(text="detailed_tomorrow")
async def detailed_weather_tomorrow(call: CallbackQuery):
    try:
        # Trying to get the weather data.
        data = get_weather_data()
    except TypeError:
        # Send this message if user asks for the weather before specifying a city.
        await call.message.answer(unspecified_city)
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
            # Write in the variable hourly weather data starting from 00:00.
            # How it works:
            # If the time is not 00:00, then in the condition ((False or False) and True) -> False;
            # If the time is 00:00, then in the condition ((True or False) and True) -> True;
            # Then "toggle" becomes True and the condition looks like this: ((False or True) and True) -> True;
            # After 24 loops, count < 24 will become False, and the condition will look
            # like this: ((False or True) and False) -> False
            if (time == '00:00' or toggle) and count < 24:
                detailed_message += f'{time}  {sign(temp)}{temp} {degree}, {description}{weather_icons[icon]} \n'
                count += 1
                toggle = True
        # Send a message indicating the weather by hour.
        await call.message.answer(detailed_message)
