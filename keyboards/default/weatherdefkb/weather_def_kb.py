from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Creating buttons that will be located at the bottom of the chat.

# Creating buttons.
weather_for_today_button = KeyboardButton("Текущая погода")
weather_for_tomorrow_button = KeyboardButton("Погода на завтра")
weather_for_a_week_button = KeyboardButton("Погода на неделю")
# Add buttons to the keyboard.
weather_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).\
    row(weather_for_today_button, weather_for_tomorrow_button).add(weather_for_a_week_button)
