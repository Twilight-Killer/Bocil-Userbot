import os

from dotenv import load_dotenv

load_dotenv(".env")

API_ID = int(os.getenv("API_ID"))

API_HASH = os.getenv("API_HASH")

BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = int(os.getenv("OWNER_ID"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))

MAX_BOT = int(os.getenv("MAX_BOT"))

OPENAI_KEY = os.getenv("OPENAI_KEY")

MONGO_URL = os.getenv("MONGO_URL")
