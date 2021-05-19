import keyboards as kb
from aiogram import types
from loader import dp


@dp.message_handler()
async def send_welcome(message: types.Message):
    await message.answer("Бот обновлен. Нажмите пожалуйста кнопку еще раз.", reply_markup=kb.weather_kb)
