from datetime import datetime, timedelta
import subprocess
import platform
import asyncio
from pyrogram import filters, __version__ as pyrogram_version
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import ubot

async def get_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return days, hours, minutes

start_time = datetime.now()

@ubot.on_message(filters.command("stats") & filters.private)
async def stats_command(client, message):
    # Get system information
    system = platform.system()
    release = platform.release()

    # Calculate uptime
    uptime_seconds = (datetime.now() - start_time).total_seconds()
    days, hours, minutes = await get_time(uptime_seconds)
    uptime_str = f"{days} hari, {hours} jam, {minutes} menit"

    # Get bot information
    total_users = len(ubot._ubot)
    owner = ""

    # Get ping to server
    server = "example.com"  # Server to ping (change this to your server)
    process = subprocess.Popen(['ping', '-c', '4', server], stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    output = stdout.decode('utf-8')
    if "64 bytes from" in output:
        ping_time = output.split("time=")[1].split(" ")[0]
        ping_server = f"{ping_time}ms"
    else:
        ping_server = "Unknown"

    # Create stats message
    stats_message = (
        f"<b>sᴛᴀᴛs ᴜʙᴏᴛ</b>\n"
        f"ᴘɪɴɢ_sᴇʀᴠᴇʀ: {ping_server}\n"
        f"ʙᴏᴛ_ᴜsᴇʀ: {total_users} user\n"
        f"ʙᴏᴛ_ᴜᴘᴛɪᴍᴇ: {uptime_str}\n"
        f"ᴘʏʀᴏɢʀᴀᴍ: {pyrogram_version}\n"
        f"ᴏᴡɴᴇʀ: {owner}\n"
      )

    # Create inline keyboard
    inline_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Button Text", callback_data="button_data")
            ]
        ]
    )

    # Reply with stats message and inline keyboard
    await message.reply(
        text=stats_message,
        reply_markup=inline_keyboard
    )
