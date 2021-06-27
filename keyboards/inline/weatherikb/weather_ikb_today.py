from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создаем кнопку, которая будет прикреплена к сообщению

# Создаем клавиатуру
detailed_today = InlineKeyboardMarkup()
# Создаем кнопку
det_today = InlineKeyboardButton(text="Подробнее", callback_data="detailed_today")
# Добавляем кнопку на клавиатуру
detailed_today.insert(det_today)
