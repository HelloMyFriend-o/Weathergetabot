if __name__ == '__main__':
    from handlers import dp
    from aiogram import executor
    from database.db import create_db
    create_db()
    executor.start_polling(dp, skip_updates=True)
