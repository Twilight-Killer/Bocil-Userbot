import random
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,
                            InputTextMessageContent)

from PyroUbot import *


async def alive_cmd(client, message):
    msg = await message.reply("<b>silahkan tunggu</b>", quote=True)
    try:
        x = await asyncio.wait_for(
            client.get_inline_bot_results(
                bot.me.username, f"alive {message.id} {client.me.id}"
            ),
            timeout=10  # Set timeout to 5 seconds
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
        await msg.delete()
    except asyncio.TimeoutError:
        await msg.edit("❌ waktu habis")
    except Exception as error:
        await msg.edit(error)


async def alive_query(client, inline_query):
    get_id = inline_query.query.split()
    for my in ubot._ubot:
        if int(get_id[2]) == my.me.id:
            try:
                peer = my._get_my_peer[my.me.id]
                users = len(peer["pm"])
                group = len(peer["gc"])
            except Exception:
                users = random.randrange(await my.get_dialogs_count())
                group = random.randrange(await my.get_dialogs_count())
            get_exp = await get_expired_date(my.me.id)
            exp = get_exp.strftime("%d-%m-%Y")
            if my.me.id == OWNER_ID:
                status = "<b>buru tani</b> <code>[bocil]</code>"
            elif my.me.id in await get_seles():
                status = "<b>buru tani</b> <code>[admin]</code>"
            else:
                status = "<b>buru tani</b>"
            button = Button.alive(get_id)
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            ub_time = await get_uptime(my.me.id)
            uptime = await get_time((time() - ub_time))
            msg = f"""
<b><a href=tg://user?id={my.me.id}>{my.me.first_name} {my.me.last_name or ''}</a>
    statud: {status} 
        expired_on: <code>{exp}</code> 
        dc_id: <code>{my.me.dc_id}</code>
        ping_dc: <code>{str(ping).replace('.', ',')} ᴍs</code>
        peer_users: <code>{users} ᴜsᴇʀs</code>
        peer_group: <code>{group} ɢʀᴏᴜᴘ</code>
        start_uptimr: <code>{uptime}</code></b>
"""
            await client.answer_inline_query(
                inline_query.id,
                cache_time=300,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="💬",
                            reply_markup=InlineKeyboardMarkup(button),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )


async def alive_close(client, callback_query):
    get_id = callback_query.data.split()
    if not callback_query.from_user.id == int(get_id[2]):
        return await callback_query.answer(
            f"❌ tombol ini bukan untuk mu {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for my in ubot._ubot:
        if callback_query.from_user.id == int(my.me.id):
            await my.delete_messages(
                unPacked.chat_id, [int(get_id[1]), unPacked.message_id]
            )
