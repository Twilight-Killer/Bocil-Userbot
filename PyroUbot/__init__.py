import logging
import os
import re
import time

from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from pyrogram.types import Message
from pyromod import listen
from pytgcalls import GroupCallFactory

from PyroUbot.config import *

# Konfigurasi logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

# Pesan debug
logging.debug("Debug message")

# Tunggu 1 detik
time.sleep(20)

def divide_numbers(a, b):
    try:
        result = a / b
        logging.debug(f"Hasil pembagian {a} / {b} adalah {result}")
        return result
    except ZeroDivisionError:
        logging.error("Tidak bisa membagi dengan nol")

# Panggil fungsi dan lakukan debugging
divide_numbers(10, 2)
divide_numbers(5, 0)

# Kelas Bot dengan logging
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

# Kelas Ubot dengan logging
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
        print(f"[𝐈𝐍𝐅𝐎] - ({self.me.id}) - 𝐒𝐓𝐀𝐑𝐓𝐄𝐃\n"
              f"Bot name: {self.me.first_name}\n"
              f"Bot username: {self.me.username}\n"
              f"prefix: {', '.join(self._prefix[self.me.id])}\n")


bot = Bot(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)
ubot = Ubot(name="ubot")


from PyroUbot.core.database import *
from PyroUbot.core.function import *
from PyroUbot.core.helpers import *
from PyroUbot.core.plugins import *
