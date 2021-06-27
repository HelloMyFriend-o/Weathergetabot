from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create buttons that will be located at the bottom of the chat.

# Create buttons.
btnWeatherToday = KeyboardButton("Текущая погода")
btnWeatherTomorrow = KeyboardButton("Погода на завтра")
btnWeatherWeek = KeyboardButton("Погода на неделю")
# Add buttons to the keyboard.
weather_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(btnWeatherToday, btnWeatherTomorrow).add(btnWeatherWeek)
