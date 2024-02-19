from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
from PyroUbot import bot, ubot
from PyroUbot.config import OWNER_ID
from datetime import datetime
import psutil
import os

@Client.on_message(filters.command("stats") & filters.private)
async def stats_command(client, message):
    uptime = datetime.now() - bot.start_time
    total_users = len(ubot._ubot)
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    uptime_str = str(uptime).split(".")[0]

    await message.reply(
        f"<b>👤 Total Users: {total_users}</b>\n"
        f"<b>🕒 Uptime: {uptime_str}</b>\n"
        f"<b>🖥️ CPU Usage: {cpu_usage}%</b>\n"
        f"<b>💾 Memory Usage: {memory_usage}%</b>\n"
        f"<b>💽 Disk Usage: {disk_usage}%</b>",
    )

@Client.on_message(filters.command("ping") & filters.private)
async def ping_command(client, message):
    start_time = datetime.now()
    await message.reply("Pong!")
    end_time = datetime.now()
    delta = (end_time - start_time).microseconds / 1000
    await message.reply(f"Ping: {delta} ms")

@Client.on_message(filters.command("uptime") & filters.private)
async def uptime_command(client, message):
    uptime = datetime.now() - bot.start_time
    uptime_str = str(uptime).split(".")[0]
    await message.reply(f"Uptime: {uptime_str}")

@Client.on_message(filters.command("serverstats") & filters.private)
async def server_stats_command(client, message):
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    await message.reply(
        f"<b>🖥️ CPU Usage: {cpu_usage}%</b>\n"
        f"<b>💾 Memory Usage: {memory_usage}%</b>\n"
        f"<b>💽 Disk Usage: {disk_usage}%</b>",
    )

@Client.on_message(filters.command("owner") & filters.private)
async def owner_command(client, message):
    owner = await client.get_users(OWNER_ID)
    await message.reply(f"Owner: {owner.first_name}")

def __MODULE__() -> str:
    return "Stats"

def __HELP__() -> str:
    return "/stats - Show bot statistics\n/ping - Check bot's response time\n/uptime - Show bot's uptime\n/serverstats - Show server statistics\n/owner - Show bot's owner"
