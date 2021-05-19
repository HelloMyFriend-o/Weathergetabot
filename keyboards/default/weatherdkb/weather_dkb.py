from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnWeatherToday = KeyboardButton("Текущая погода")
btnWeatherTomorrow = KeyboardButton("Погода на завтра")
btnWeatherWeek = KeyboardButton("Погода на неделю")

weather_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(btnWeatherToday, btnWeatherTomorrow).add(btnWeatherWeek)
