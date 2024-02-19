import asyncio
from datetime import datetime
from gc import get_objects
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *


async def send_msg_to_owner(client, message):
    if message.from_user.id != OWNER_ID:
        buttons = [
            [
                InlineKeyboardButton(
                    "👤 ᴘʀᴏꜰɪʟ", callback_data=f"profil {message.from_user.id}"
                ),
                InlineKeyboardButton(
                    "ᴊᴀᴡᴀʙ 💬", callback_data=f"jawab_pesan {message.from_user.id}"
                ),
            ],
            [
                InlineKeyboardButton(
                    "sᴀᴛᴜ ʙᴜʟᴀɴ", callback_data=f"success {message.from_user.id} 1"
                )
            ],
        ]
        user_link = f"<a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
        formatted_text = f"{user_link}\n\n<code>{message.text}</code>"

        await client.send_message(
            OWNER_ID, formatted_text, reply_markup=InlineKeyboardMarkup(buttons)
        )


async def ping_cmd(client, message):
    uptime = await get_time((time() - start_time))
    start = datetime.now()
    delta_ping_formatted = "{:.3f}".format(delta_ping)
   
    ping_task = asyncio.create_task(client.invoke(Ping(ping_id=0)))
    emot_1_task = asyncio.create_task(get_vars(client.me.id, "EMOJI_PING_PONG"))
    emot_2_task = asyncio.create_task(get_vars(client.me.id, "EMOJI_UPTIME"))
    emot_3_task = asyncio.create_task(get_vars(client.me.id, "EMOJI_MENTION"))

    await asyncio.wait([ping_task, emot_1_task, emot_2_task, emot_3_task], return_when=asyncio.ALL_COMPLETED)

    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000

    emot_1 = emot_1_task.result()
    emot_2 = emot_2_task.result()
    emot_3 = emot_3_task.result()

    emot_pong = emot_1 if emot_1 else "5269563867305879894"
    emot_uptime = emot_2 if emot_2 else "5316615057939897832"
    emot_mention = emot_3 if emot_3 else "6226371543065167427"

    if client.me.is_premium:
    _ping = f"""
    <b><emoji id={emot_pong}>🏓</emoji> ᴘᴏɴɢ:</b> <code>{delta_ping_formatted.replace('.', ',')} ms</code>
    <b><emoji id={emot_uptime}>⏰</emoji> ᴜᴘᴛɪᴍᴇ:</b> <code>{uptime}</code>
    <b><emoji id={emot_mention}>👑</emoji> ᴍᴇɴᴛɪᴏɴ:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
    """
else:
    _ping = f"""
    <b>❏ ᴋᴇᴄᴇᴘᴀᴛᴀɴ ᴊᴀʀɪɴɢᴀɴ<b>
    <b>├ 𝟻+:</b> <code>{delta_ping_formatted.replace('.', ',')} ms</code>
    <b>├ ᴛɪᴍᴇ:</b> <code>{uptime}</code>
    <b>╰ ᴊᴇɴᴇɴɢ:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
    """

await message.reply(_ping)

async def start_cmd(client, message):
    await send_msg_to_owner(client, message)
    if len(message.command) < 2:
        buttons = Button.start(message)
        msg = MSG.START(message)
        await message.reply(msg, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        txt = message.text.split(None, 1)[1]
        msg_id = txt.split("_", 1)[1]
        send = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ...</b>")
        if "secretMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ ᴇʀʀᴏʀ:</b> <code>{error}</code>")
            user_or_me = [m.reply_to_message.from_user.id, m.from_user.id]
            if message.from_user.id not in user_or_me:
                return await send.edit(
                    f"<b>❌ ᴘᴇsᴀɴ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋᴍᴜ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
                )
            else:
                text = await client.send_message(
                    message.chat.id,
                    m.text.split(None, 1)[1],
                    protect_content=True,
                    reply_to_message_id=message.id,
                )
                await send.delete()
                await asyncio.sleep(120)
                await message.delete()
                await text.delete()
        elif "copyMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ ᴇʀʀᴏʀ:</b> <code>{error}</code>")
            id_copy = int(m.text.split()[1].split("/")[-1])
            if "t.me/c/" in m.text.split()[1]:
                chat = int("-100" + str(m.text.split()[1].split("/")[-2]))
            else:
                chat = str(m.text.split()[1].split("/")[-2])
            try:
                get = await client.get_messages(chat, id_copy)
                await get.copy(message.chat.id, reply_to_message_id=message.id)
                await send.delete()
            except Exception as error:
                await send.edit(error)
