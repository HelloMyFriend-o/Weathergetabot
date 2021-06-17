import requests
from aiogram import types
from config import APPID
from database.db import connect_db


# Возвращает данные о погоде в формате json
def url_weather():
    # Подключаемся к БД
    con = connect_db()
    cur = con.cursor()

    # Получаем данные о пользователе, который написал сообщение
    user = types.User.get_current()
    # Выбираем долготу и широту по id пользователя, и помещаем их в переменные
    cur.execute("SELECT lat FROM users WHERE user_id = %s", (user.id,))
    lat_tuple = cur.fetchone()
    cur.execute("SELECT lon FROM users WHERE user_id = %s", (user.id,))
    lon_tuple = cur.fetchone()

    # Отключение от БД
    con.commit()
    con.close()
    # tuple -> float
    lat = float(''.join(map(str, lat_tuple)))
    lon = float(''.join(map(str, lon_tuple)))
    # Указываем, какие данные нас не интересуют (минуты, оповещения)
    exclude = 'minutely,alerts'
    # Указываем язык
    lang = 'ru'
    # Указываем единицы измерения
    units = 'metric'
    # Делаем запрос о погоде
    r = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?"
                     f"lat={lat}&lon={lon}&exclude={exclude}&lang={lang}&units={units}&appid={APPID}")
    return r.json()
