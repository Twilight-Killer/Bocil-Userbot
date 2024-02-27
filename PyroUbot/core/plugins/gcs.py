import asyncio
from gc import get_objects
import time

from pyrogram.errors import FloodWait

from PyroUbot import *


async def broadcast_group_cmd(client, message):
    msg = await message.reply("<emoji id=5971865795582495562>🔺</emoji> sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ..." if client.me.is_premium else "sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ...", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("<emoji id=6226399941388928924>👓</emoji> ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ" if client.me.is_premium else "ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")

    chats = await get_global_id(client, "group")
    blacklist = await get_chat(client.me.id)

    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id in blacklist:
            continue

        try:
            await asyncio.sleep(1.5)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            failed += 1

    await msg.delete()
    return await message.reply(
        f"<b><emoji id=5895735846698487922>🌐</emoji> ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ sᴇʟᴇsᴀɪ</b>\n<b> <emoji id=5021905410089550576>✅</emoji> ʙᴇʀʜᴀsɪʟ ᴋᴇ; {done} ɢʀᴏᴜᴘ</b>\n<b> <emoji id=5019523782004441717>❌</emoji> ɢᴀɢᴀʟ ᴋᴇ: {failed} ɢʀᴏᴜᴘ</b>" if client.me.is_premium else f"<b>❏ ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ sᴇʟᴇsᴀɪ</b>\n<b> ├ ʙᴇʀʜᴀsɪʟ ᴋᴇ; {done} ɢʀᴏᴜᴘ</b>\n<b> ╰ ɢᴀɢᴀʟ ᴋᴇ: {failed} ɢʀᴏᴜᴘ</b>",
        quote=True,
    )


async def broadcast_users_cmd(client, message):
    msg = await message.reply("<emoji id=5971865795582495562>🔺</emoji> sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ..." if client.me.is_premium else "sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ...", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("<emoji id=6226399941388928924>👓</emoji> ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ" if client.me.is_premium else "ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ")

    chats = await get_global_id(client, "users")

    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id == client.me.id:
            continue

        try:
            await asyncio.sleep(1.5)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            failed += 1

    await msg.delete()
    return await message.reply(
        f"<b><emoji id=5895735846698487922>🌐</emoji> ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ sᴇʟᴇsᴀɪ</b>\n<b> <emoji id=5021905410089550576>✅</emoji> ʙᴇʀʜᴀsɪʟ ᴋᴇ; {done} ᴜsᴇʀs</b>\n<b> <emoji id=5019523782004441717>❌</emoji> ɢᴀɢᴀʟ ᴋᴇ: {failed} ᴜsᴇʀs</b>" if client.me.is_premium else f"<b>❏ ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ sᴇʟᴇsᴀɪ</b>\n<b> ├ ʙᴇʀʜᴀsɪʟ ᴋᴇ; {done} ᴜsᴇʀs</b>\n<b> ╰ ɢᴀɢᴀʟ ᴋᴇ: {failed} ᴜsᴇʀs</b>",
        quote=True,
    )



async def send_msg_cmd(client, message):
    if message.reply_to_message:
        chat_id = (
            message.chat.id if len(message.command) < 2 else message.text.split()[1]
        )
        try:
            if client.me.id != bot.me.id:
                if message.reply_to_message.reply_markup:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"get_send {id(message)}"
                    )
                    return await client.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
        except Exception as error:
            return await message.reply(error)
        else:
            try:
                return await message.reply_to_message.copy(chat_id)
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("ᴋᴇᴛɪᴋ ʏᴀɴɢ ʙᴇɴᴇʀ")
        chat_id, chat_text = message.text.split(None, 2)[1:]
        try:
            return await client.send_message(chat_id, chat_text)
        except Exception as t:
            return await message.reply(f"{t}")


async def send_inline(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = next((obj for obj in get_objects() if id(obj) == _id), None)
    if m:
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ],
        )


# Enable/disable auto-gcast
AUTO_GCAST_ENABLED = True

# Auto-gcast settings
AUTO_GCAST_LIMIT = 5  # Maximum number of auto-gcasts per interval
AUTO_GCAST_TEXT = "Hello, this is an auto-gcast message!"  # Auto-gcast message
AUTO_GCAST_DELAY = 60  # Auto-gcast interval in seconds

# Auto-gcast list
AUTO_GCAST_LIST = []

# Function to send auto-gcast message
async def send_auto_gcast(client):
    for chat_id in AUTO_GCAST_LIST:
        await client.send_message(chat_id, AUTO_GCAST_TEXT)

# Auto-gcast loop
async def auto_gcast_loop(client):
    while AUTO_GCAST_ENABLED:
        await send_auto_gcast(client)
        time.sleep(AUTO_GCAST_DELAY)

# Command to enable/disable auto-gcast
@PY.UBOT("autogcast")
async def toggle_auto_gcast(_, message):
    global AUTO_GCAST_ENABLED
    AUTO_GCAST_ENABLED = not AUTO_GCAST_ENABLED
    if AUTO_GCAST_ENABLED:
        await message.reply("Auto-gcast enabled!")
        await auto_gcast_loop(message._client)
    else:
        await message.reply("Auto-gcast disabled!")

# Command to set auto-gcast text
@PY.UBOT("setgcast")
async def set_auto_gcast_text(_, message):
    global AUTO_GCAST_TEXT
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        AUTO_GCAST_TEXT = args[1]
        await message.reply(f"Auto-gcast text set to: {AUTO_GCAST_TEXT}")
    else:
        await message.reply("Usage: /setgcast [text]")

# Command to add chat to auto-gcast list
@PY.UBOT("addgcast")
async def add_auto_gcast_chat(_, message):
    global AUTO_GCAST_LIST
    chat_id = message.chat.id
    if chat_id not in AUTO_GCAST_LIST:
        AUTO_GCAST_LIST.append(chat_id)
        await message.reply("Chat added to auto-gcast list!")
    else:
        await message.reply("Chat is already in auto-gcast list!")

# Command to remove chat from auto-gcast list
@PY.UBOT("removegcast")
async def remove_auto_gcast_chat(_, message):
    global AUTO_GCAST_LIST
    chat_id = message.chat.id
    if chat_id in AUTO_GCAST_LIST:
        AUTO_GCAST_LIST.remove(chat_id)
        await message.reply("Chat removed from auto-gcast list!")
    else:
        await message.reply("Chat is not in auto-gcast list!")
