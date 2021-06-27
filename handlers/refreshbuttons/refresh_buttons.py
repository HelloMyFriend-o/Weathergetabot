from aiogram import types

from loader import dp
import keyboards as kb


# Triggered when user enter the command "/buttons".
@dp.message_handler(commands=['buttons'])
async def send_welcome(message: types.Message):
    await message.answer("Кнопки обновлены", reply_markup=kb.weather_kb)
