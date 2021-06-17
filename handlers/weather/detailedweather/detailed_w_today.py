import datetime
from aiogram.types import CallbackQuery
from loader import dp
from ..config import *
from ..url_weather import url_weather


# Срабатывает при нажатии на кнопку "Подробнее" после запроса "Текущей погоды"
@dp.callback_query_handler(text="detailed_today")
async def detailed_weather_today(call: CallbackQuery):
    try:
        # Пробуем получить данные о погоде
        data = url_weather()
    except TypeError:
        pass
    else:
        detailed_message = f'Давление: {round(data["daily"][0]["pressure"] * hpa_to_mmhg)} мм рт.ст.\n' \
                           f'Влажность: {data["daily"][0]["humidity"]} % \n\n'
        # В полученных данных указана погода для следующих 48 часов. Отображаем только первые 24
        for hour in data['hourly'][:-24]:
            time = datetime.datetime.fromtimestamp(hour["dt"]).strftime('%H:%M')
            temp = round(hour["temp"])
            description = hour["weather"][0]["description"]
            icon = hour["weather"][0]["icon"]
            detailed_message += f'{time}  {sign(temp)}{temp} {degree}, {description}{weather_icons[icon]} \n'
        # Выводим сообщение с погодой указанной по часам
        await call.message.answer(detailed_message)
