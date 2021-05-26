import logging
import locale
from config import API_TOKEN, WEBHOOK_HOST, WEBHOOK_PATH
from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()


locale.setlocale(locale.LC_ALL, "ru_RU.utf8")
