from aiogram import types
from config import ADMIN_ID
from database.db import connect_db
from loader import dp


@dp.message_handler(commands=["users"])
async def users_quantity(message: types.Message):
    user = types.User.get_current()
    user_id = user.id

    if user_id == int(ADMIN_ID):
        con = connect_db()
        cur = con.cursor()

        cur.execute("SELECT id, first_name, last_name, city FROM users")
        users = cur.fetchall()
        users_quantity_msg = "Пользователи:\n\n"

        for number, first_name, last_name, city in users:
            users_quantity_msg += f'{number}. {first_name} {last_name}:   {city}\n'
        await message.answer(users_quantity_msg)

        con.commit()
        con.close()
    else:
        pass
