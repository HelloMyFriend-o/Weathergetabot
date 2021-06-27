from aiogram import types

from loader import dp


# Срабатывает при первом запуске бота или при вводе команды "/start"
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Здравствуйте 🤖\n"
                         "Напишите интересующий Вас город.\n\n"
                         "Например:\n"
                         "город Казань\n"
                         "город Санкт-Петербург\n"
                         "город Нижний Новгород")
