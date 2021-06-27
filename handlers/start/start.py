from aiogram import types

from loader import dp


# Triggered when bot is first launched or when the "/start" command is entered.
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Здравствуйте 🤖\n"
                         "Напишите интересующий Вас город.\n\n"
                         "Например:\n"
                         "город Казань\n"
                         "город Санкт-Петербург\n"
                         "город Нижний Новгород")
