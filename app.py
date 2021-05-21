if __name__ == '__main__':
    from handlers import dp
    from aiogram import executor
    from database.db import create_tb

    create_tb()
    executor.start_polling(dp, skip_updates=True)
