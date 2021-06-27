from aiogram import types

from loader import dp, ADMIN_ID
from database.db import connect_db


# Triggered when user enter the command "/users".
@dp.message_handler(commands=["users"])
async def users_quantity(message: types.Message):
    # Getting data about user who wrote the message.
    user = types.User.get_current()
    user_id = user.id

    if str(user_id) in ADMIN_ID:
        # Connecting to the DB.
        con = connect_db()
        cur = con.cursor()
        # Selecting first names, last names and cities of all users and placing them in the "users".
        cur.execute("SELECT first_name, last_name, city FROM users")
        users = cur.fetchall()
        users_quantity_msg = "Пользователи:\n\n"

        number = 0
        # The loop iterates over all users, and add first name, last name and city
        # of each of them to the "users_quantity_msg".
        for first_name, last_name, city in users:
            number += 1
            users_quantity_msg += f'{number}. {first_name} {last_name}:   {city}\n'

        # Send a message with a list of users.
        await message.answer(users_quantity_msg)

        # Disconnecting from the DB.
        con.commit()
        con.close()
