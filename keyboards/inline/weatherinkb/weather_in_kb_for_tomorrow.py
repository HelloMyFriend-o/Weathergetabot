from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Creating a button that will be attached to the message.

# Creating a keyboard.
detailed_weather_for_tomorrow_keyboard = InlineKeyboardMarkup()
# Creating a button.
detailed_weather_for_tomorrow_button = InlineKeyboardButton(text="Подробнее",
                                                            callback_data="detailed_weather_for_tomorrow_keyboard")
# Add buttons to the keyboard.
detailed_weather_for_tomorrow_keyboard.insert(detailed_weather_for_tomorrow_button)
