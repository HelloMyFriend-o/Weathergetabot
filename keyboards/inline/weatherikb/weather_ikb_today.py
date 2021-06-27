from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Create a button that will be attached to the message.

# Create keyboard.
detailed_today = InlineKeyboardMarkup()
# Create button.
det_today = InlineKeyboardButton(text="Подробнее", callback_data="detailed_today")
# Add buttons to the keyboard.
detailed_today.insert(det_today)
