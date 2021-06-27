from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Create a button that will be attached to the message.

# Create keyboard.
detailed_tomorrow = InlineKeyboardMarkup()
# Create button.
det_today = InlineKeyboardButton(text="Подробнее", callback_data="detailed_tomorrow")
# Add buttons to the keyboard.
detailed_tomorrow.insert(det_today)
