# Telegram weather bot

1. Clone the repository:
```bash
git clone https://github.com/HelloMyFriend-o/Weathergetabot.git
```
2. Create and activate a virtual environment

3. Install dependencies from file ***requirements.txt***:
```bash
pip install -r requirements.txt
```
4. Rename the file from ***.env(example)*** to ***.env***

5. Create Telegram bot, get TOKEN and assign it to the **API_TOKEN** variable in ***.env***

6. Registrate at ***openweathermap.org***, get APPID and assign it to the variable of the same name in ***.env*** 

7. Download ngrok, run, and enter the command:

```bash
ngrok http 3000
```

8. Copy adress witch starts with ***https*** (like this: https://12a3-4-56-78-901.ngrok.io/) and assign it to the **WEBHOOK_HOST** variable in **.env**

6. Create DB PostgreSQL and fill in the corresponding variables in the file ***.env***

7. Run the app:
```bash
python app.py
```

# Commands:

/city - shows the city selected by the user

/buttons - displays buttons if they suddenly disappeared

/users - shows a list of bot users (for this command to work, add your Telegram id in **ADMIN_ID** variable in ***.env***)
