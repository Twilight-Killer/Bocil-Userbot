import subprocess
import psutil
import platform
import time
from datetime import datetime
from pyrogram import filters

from PyroUbot import *

@ubot.on_message(filters.command("stats") & FILTERS.PRIVATE)
async def stats_command(client, message):
    # Get system information
    system = platform.system()
    release = platform.release()
    pyrogram_version = platform.python_version()
    uptime_seconds = time.time() - ubot.start_time
    uptime_str = str(datetime.timedelta(seconds=uptime_seconds))

    # Get bot information
    total_users = len(ubot._ubot)
    owner = "kulbetsss.t.me"

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
        f"<b>SYSTEM UBOT</b>\n"
        f"ᴘɪɴɢ_sᴇʀᴠᴇʀ: {ping_server}\n"
        f"ʙᴏᴛ_ᴜsᴇʀ: {total_users} user\n"
        f"ʙᴏᴛ_ᴜᴘᴛɪᴍᴇ: {uptime_str}\n"
        f"ᴘʏʀᴏɢʀᴀᴍ: {pyrogram_version}\n"
        f"ᴏᴡɴᴇʀ: {owner}"
    )

    # Reply with stats message
    await message.reply(stats_message, parse_mode="html")
