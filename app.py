from config import WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
from handlers import dp
from database.db import create_tb
from aiogram.utils.executor import start_webhook
from loader import on_startup, on_shutdown

if __name__ == '__main__':
    create_tb()
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
