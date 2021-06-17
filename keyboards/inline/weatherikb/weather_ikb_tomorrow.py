from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создаем кнопку, которая будет прикреплена к сообщению

# Создаем клавиатуру
detailed_tomorrow = InlineKeyboardMarkup()

# Создаем кнопку
det_today = InlineKeyboardButton(text="Подробнее", callback_data="detailed_tomorrow")

# Добавляем кнопку на клавиатуру
detailed_tomorrow.insert(det_today)
