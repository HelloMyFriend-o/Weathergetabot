import datetime
from aiogram.types import CallbackQuery
from loader import dp
from ..config import *
from ..url_weather import url_weather


# Срабатывает при нажатии на кнопку "Подробнее" после запроса "Погода на завтра"
@dp.callback_query_handler(text="detailed_tomorrow")
async def detailed_weather_tomorrow(call: CallbackQuery):
    try:
        # Пробуем получить данные о погоде
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
            # Записываем в переменную почасовые данные о погоде начиная с 00:00.
            # Работает следующим образом:
            # Если время не 00:00, то в условии ((False or False) and True) -> False;
            # Если время 00:00, то в условии ((True or False) and True) -> True;
            # Далее "toggle" становится True и условие выглядит так: ((False or True) and True) -> True;
            # Через 24 цикла count < 24 примет значение False, и условие будет
            # выглядеть так: ((False or True) and False) -> False
            if (time == '00:00' or toggle) and count < 24:
                detailed_message += f'{time}  {sign(temp)}{temp} {degree}, {description}{weather_icons[icon]} \n'
                count += 1
                toggle = True
        # Выводим сообщение с погодой указанной по часам
        await call.message.answer(detailed_message)
