from datetime import datetime, timedelta
import subprocess
import platform
import asyncio
from pyrogram import filters, __version__ as pyrogram_version
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import ubot

@ubot.on_message(filters.command("stats") & filters.user)
async def stats_command(client, message):
    # Get system information
    system = platform.system()
    release = platform.release()

    # Calculate uptime
    uptime_delta = datetime.now() - start_time
    uptime_str = str(uptime_delta).split(".")[0]

    # Get bot information
    total_users = len(ubot._ubot)

    # Get ping to server
    server = "example.com"  # Server to ping (change this to your server)
    ping_task = asyncio.create_task(ping_server(server))

    # Get owner information
    owner = "pemilik saham telegram"  # Change this to your bot owner's name

    # Wait for all tasks to complete
    ping_result = await ping_task

    # Create stats message
    stats_message = (
        f"<b>sᴛᴀᴛs ᴜʙᴏᴛ</b>\n"
        f"ᴘɪɴɢ_sᴇʀᴠᴇʀ: {ping_result}\n"
        f"ʙᴏᴛ_ᴜsᴇʀ: {total_users} user\n"
        f"ʙᴏᴛ_ᴜᴘᴛɪᴍᴇ: {uptime_str}\n"
        f"ᴘʏʀᴏɢʀᴀᴍ: {pyrogram_version}\n"
        f"ᴏᴡɴᴇʀ: {owner}\n"
    )

    # Create InlineKeyboardButton
    button_text = "Click Me!"
    button_callback_data = "button_clicked"
    button = InlineKeyboardButton(button_text, callback_data=button_callback_data)

    # Create InlineKeyboardMarkup with the button
    reply_markup = InlineKeyboardMarkup([[button]])

    # Reply with stats message and button
    await message.reply(stats_message, reply_markup=reply_markup)
