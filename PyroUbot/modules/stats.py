from datetime import datetime
import platform
import asyncio
import subprocess
from pyrogram import filters, __version__ as pyrogram_version
from PyroUbot import bot

start_time = datetime.now()

async def get_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return days, hours, minutes

async def ping_server(server):
    process = await asyncio.create_subprocess_exec('ping', '-c', '4', server, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await process.communicate()
    output = stdout.decode('utf-8')
    if "64 bytes from" in output:
        ping_time = output.split("time=")[1].split(" ")[0]
        return f"{ping_time}ms"
    else:
        return "Unknown"

@bot.on_message(filters.command("stats") & filters.me)
async def stats_command(client, message):
    # Get system information
    system = platform.system()
    release = platform.release()

    # Calculate uptime
    uptime_seconds = (datetime.now() - start_time).total_seconds()
    days, hours, minutes = await get_time(uptime_seconds)
    uptime_str = f"{days} hari, {hours} jam, {minutes} menit"

    # Get bot information
    total_users = len(bot._bot)

    # Get ping to server
    server = "example.com"  # Server to ping (change this to your server)
    ping_result = await ping_server(server)

    # Get owner information
    owner = "ㅤ Pemilik saham tele"  # Change this to your bot owner's name

    # Create stats message
    stats_message = (
        f"<b>sᴛᴀᴛs ʙᴏᴛ</b>\n"
        f"ᴘɪɴɢ_sᴇʀᴠᴇʀ: {ping_result}\n"
        f"ʙᴏᴛ_ᴜsᴇʀ: {total_users} user\n"
        f"ʙᴏᴛ_ᴜᴘᴛɪᴍᴇ: {uptime_str}\n"
        f"ᴘʏʀᴏɢʀᴀᴍ: {pyrogram_version}\n"
        f"ᴏᴡɴᴇʀ: {owner}\n"
    )

    # Reply with stats message
    await message.reply(stats_message)
