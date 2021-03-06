import locale
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

locale.setlocale(locale.LC_ALL, "ru_RU.utf8")

load_dotenv()

API_TOKEN = str(os.getenv("API_TOKEN"))
APPID = str(os.getenv("APPID"))

ADMIN_ID = os.getenv("ADMIN_ID").split(', ')

WEBHOOK_HOST = str(os.getenv("WEBHOOK_HOST"))
WEBHOOK_PATH = str(os.getenv("WEBHOOK_PATH"))

WEBAPP_HOST = str(os.getenv("WEBAPP_HOST"))
WEBAPP_PORT = str(os.getenv("WEBAPP_PORT"))

PG_DB = str(os.getenv("PG_DB"))
PG_USER = str(os.getenv("PG_USER"))
PG_PASS = str(os.getenv("PG_PASS"))
PG_HOST = str(os.getenv("PG_HOST"))
PG_PORT = str(os.getenv("PG_PORT"))

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
