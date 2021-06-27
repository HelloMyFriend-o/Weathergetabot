from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Creating a button that will be attached to the message.

# Creating a keyboard.
detailed_today = InlineKeyboardMarkup()
# Creating a button.
det_today = InlineKeyboardButton(text="Подробнее", callback_data="detailed_today")
# Add buttons to the keyboard.
detailed_today.insert(det_today)
