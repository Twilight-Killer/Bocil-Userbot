import logging
import os
import re
import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from pyrogram.types import Message
from pytgcalls import GroupCallFactory

logger = logging.getLogger(__name__)
# from pyromod import listen

from PyroUbot.config import *


class ConnectionError(Exception):
    pass

class ConnectionHandler(logging.Handler):
    def emit(self, record):
        for error_type in ["OSErro", "TimeoutError"]:
            if error_type in record.getMessage():
                self.handle_error(record.getMessage())

    def handle_error(self, error_message):
        self.log_error(error_message)
        raise ConnectionError(error_message)

    def log_error(self, error_message):
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"Error: {error_message}\n")


logging.basicConfig(level=logging.ERROR, format='%(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
handler = ConnectionHandler()
logger.addHandler(handler)

max_retries = 3
retries = 0

while retries < max_retries:
    try:
        raise OSError("Koneksi Gagal")
    except OSError as e:
        logger.error(f"Terjadi kesalahan: {e}")
        retries += 1
        if retries < max_retries:
            logger.info(f"Mencoba kembali... (percobaan ke-{retries})")
            continue  
        else:
            logger.info("Gagal setelah beberapa percobaan.")
            break

async def get_channel_messages(channel, bot):
    try:
        messages = await bot.get_messages(channel)
        return messages
    except FloodWait as e:
        await asyncio.sleep(e.x)
        messages = await get_channel_messages(channel, bot)
        return messages

class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.device_model="BuruTaniUbot"

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func
        return decorator

    def on_callback_query(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(CallbackQueryHandler(func, filters), group)
            return func
        return decorator

    async def start(self):
        await super().start()


class Ubot(Client):
    _ubot = []
    _prefix = {}
    _get_my_id = []
    _translate = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.device_model="BuruTaniUbot"
        self.group_call = GroupCallFactory(self).get_file_group_call("input.raw")

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func
        return decorator

    def set_prefix(self, user_id, prefix):
        self._prefix[user_id] = prefix

    async def get_prefix(self, user_id):
        return self._prefix.get(user_id, [".", ",", ":", ";", "!"])

    def cmd_prefix(self, cmd):
        command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")

        async def func(_, client, message):
            if message.text:
                text = message.text.strip().encode("utf-8").decode("utf-8")
                username = client.me.username or ""
                prefixes = await self.get_prefix(client.me.id)

                if not text:
                    return False

                for prefix in prefixes:
                    if not text.startswith(prefix):
                        continue

                    without_prefix = text[len(prefix) :]

                    for command in cmd.split("|"):
                        if not re.match(
                            rf"^(?:{command}(?:@?{username})?)(?:\s|$)",
                            without_prefix,
                            flags=re.IGNORECASE | re.UNICODE,
                        ):
                            continue

                        without_command = re.sub(
                            rf"{command}(?:@?{username})?\s?",
                            "",
                            without_prefix,
                            count=1,
                            flags=re.IGNORECASE | re.UNICODE,
                        )
                        message.command = [command] + [
                            re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                            for m in command_re.finditer(without_command)
                        ]

                        return True

                return False

        return filters.create(func)

    async def start(self):
        await super().start()
        handler = await get_pref(self.me.id)
        if handler:
            self._prefix[self.me.id] = handler
        else:
            self._prefix[self.me.id] = [".", ",", ":", ";", "!"]
        self._ubot.append(self)
        self._get_my_id.append(self.me.id)
        self._translate[self.me.id] = "id"
        logger.info(f"[𝐈𝐍𝐅𝐎] - ({self.me.id}) - 𝐒𝐓𝐀𝐑𝐓𝐄𝐃\n"
              f"Bot name: {self.me.first_name}\n"
              f"Bot username: {self.me.username}\n"
              f"prefix: {', '.join(self._prefix[self.me.id])}\n")


bot = Bot(
    name="bot_session",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=False,
)
ubot = Ubot(name="ubot")


from PyroUbot.core.database import *
from PyroUbot.core.function import *
from PyroUbot.core.helpers import *
from PyroUbot.core.plugins import *
