from datetime import datetime as dt
import psutil

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PyroUbot import bot, OWNER_ID

from PyroUbot import *

@bot.on_message(filters.command("stats") & filters.private)
async def stats_command(client, message):
    uptime = dt.now() - bot.start_time
    total_users = len(ubot._ubot)
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    uptime_str = str(uptime).split(":")[0]

    await message.reply(
        f"<b>👤 Total Users: {total_users}</b>\n"
        f"<b>🕒 Uptime: {uptime_str}</b>\n"
        f"<b>🖥️ CPU Usage: {cpu_usage}%</b>\n"
        f"<b>💾 Memory Usage: {memory_usage}%</b>\n"
        f"<b>💽 Disk Usage: {disk_usage}%</b>",
    )

@bot.on_message(filters.command("owner") & filters.private)
async def owner_command(client, message):
    owner = await bot.get_users(OWNER_ID)
    await message.reply(f"Owner: {owner.first_name}")

def __MODULE__() -> str:
    return "Stats"

def __HELP__() -> str:
    return "/stats - Show bot statistics\n/ping - Check bot's response time\n/uptime - Show bot's uptime\n/serverstats - Show server statistics\n/owner - Show bot's owner"
