from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

detailed_today = InlineKeyboardMarkup()

det_today = InlineKeyboardButton(text="Подробнее", callback_data="detailed_today")
detailed_today.insert(det_today)
