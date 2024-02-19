from datetime import datetime
import platform
import asyncio
import subprocess
from pyrogram import filters, __version__ as pyrogram_version

from PyroUbot import ubot

start_time = datetime.now()

@ubot.on_message(filters.command("stats") | filters.private)
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
    owner = "Owner Name"  # Change this to your bot owner's name

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

    # Reply with stats message
    await message.reply(stats_message)

async def ping_server(server):
    process = await asyncio.create_subprocess_exec('ping', '-c', '4', server, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await process.communicate()
    output = stdout.decode('utf-8')
    if "64 bytes from" in output:
        ping_time = output.split("time=")[1].split(" ")[0]
        return f"{ping_time}ms"
    else:
        return "Unknown"
