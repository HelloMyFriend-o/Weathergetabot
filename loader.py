import logging
import locale
from config import API_TOKEN
from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

locale.setlocale(locale.LC_ALL, "ru_RU.utf8")
# for Windows "ru"
# for Ubuntu "ru_RU.utf8"
