from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

detailed_tomorrow = InlineKeyboardMarkup()

det_today = InlineKeyboardButton(text="Подробнее", callback_data="detailed_tomorrow")
detailed_tomorrow.insert(det_today)
