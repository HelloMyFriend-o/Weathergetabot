import os

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = str(os.getenv("API_TOKEN"))
APPID = str(os.getenv("APPID"))

ADMIN_ID = str(os.getenv("ADMIN_ID"))

PG_DB = str(os.getenv("PG_DB"))
PG_USER = str(os.getenv("PG_USER"))
PG_PASS = str(os.getenv("PG_PASS"))
PG_HOST = str(os.getenv("PG_HOST"))
PG_PORT = str(os.getenv("PG_PORT"))
