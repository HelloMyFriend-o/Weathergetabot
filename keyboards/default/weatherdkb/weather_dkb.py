from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем кнопки, которые будут располагаться внизу чата


# Создание кнопок
btnWeatherToday = KeyboardButton("Текущая погода")
btnWeatherTomorrow = KeyboardButton("Погода на завтра")
btnWeatherWeek = KeyboardButton("Погода на неделю")

# Добавление кнопок на клавиатуру
weather_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(btnWeatherToday, btnWeatherTomorrow).add(btnWeatherWeek)
