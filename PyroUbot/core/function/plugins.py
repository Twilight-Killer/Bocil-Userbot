from importlib import import_module
from platform import python_version

from pyrogram import __version__
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import bot, ubot
from PyroUbot.config import OWNER_ID
from PyroUbot.core.helpers import PY
from PyroUbot.modules import loadModule

HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = import_module(f"PyroUbot.modules.{mod}")
        if hasattr(imported_module, "__MODULE__") and isinstance(imported_module.__MODULE__, str):
            HELP_COMMANDS[imported_module.__MODULE__.replace(" ", "_").lower()] = imported_module
    print(f"[🤖 @{bot.me.username} 🤖] [🔥 TELAH BERHASIL DIAKTIFKAN! 🔥]")

async def sendStartupMessage():
    await bot.send_message(
        OWNER_ID,
        f"""
<b>🤖 {bot.me.mention} ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪꜰᴋᴀɴ</b>

<b>📁 ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS)}</b>
<b>📘 ᴘʏᴛʜᴏɴ: {python_version()}</b>
<b>📙 ᴘʏʀᴏɢʀᴀᴍ: {__version__}</b>

<b>👤 ᴜsᴇʀʙᴏᴛ: {len(ubot._ubot)}</b>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🤖 ʟɪsᴛ ᴜsᴇʀʙᴏᴛ 🤖", callback_data="cek_ubot")],
            ]
        ),
    )

@PY.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
