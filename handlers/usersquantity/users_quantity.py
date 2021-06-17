from aiogram import types
from config import ADMIN_ID
from database.db import connect_db
from loader import dp


# Срабатывает при вводе команды "/city"
@dp.message_handler(commands=["users"])
async def users_quantity(message: types.Message):
    # Получаем данные о пользователе, который написал сообщение (id)
    user = types.User.get_current()
    user_id = user.id
    # True, если id пользователя есть в списке id админов
    if user_id == int(ADMIN_ID):
        # Подключаемся к БД
        con = connect_db()
        cur = con.cursor()
        # Выбираем имена, фамилии и города всех пользователей и помещаем в переменную "users"
        cur.execute("SELECT first_name, last_name, city FROM users")
        users = cur.fetchall()
        users_quantity_msg = "Пользователи:\n\n"

        number = 0
        # В цикле перебираем всех пользователей, и добавляем имя, фамилию и город каждого из них
        # в переменную "users_quantity_msg"
        for first_name, last_name, city in users:
            number += 1
            users_quantity_msg += f'{number}. {first_name} {last_name}:   {city}\n'

        # Выводим сообщение со списком пользователей
        await message.answer(users_quantity_msg)

        # Отключаемся от БД
        con.commit()
        con.close()
