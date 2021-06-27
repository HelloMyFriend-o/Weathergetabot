from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Creating a button that will be attached to the message.

# Creating a keyboard.
detailed_tomorrow = InlineKeyboardMarkup()
# Creating a button.
det_today = InlineKeyboardButton(text="Подробнее", callback_data="detailed_tomorrow")
# Add buttons to the keyboard.
detailed_tomorrow.insert(det_today)
