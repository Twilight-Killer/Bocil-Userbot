import asyncio
from gc import get_objects

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


auto_gcast_on = False
auto_gcast_text = "Hello, this is an auto-gcast message!"
auto_gcast_delay = 5

# Auto-gcast function
async def auto_gcast():
    global auto_gcast_on
    global auto_gcast_text
    global auto_gcast_delay

    while auto_gcast_on:
        async for dialog in():
            try:
                await app.send_message(dialog.chat.id, auto_gcast_text)
            except Exception as e:
                print(f"Failed to send message to {dialog.chat.id}: {e}")
        await asyncio.sleep(auto_gcast_delay)


async def toggle_auto_gcast(_, message):
    global auto_gcast_on
    global auto_gcast_text
    global auto_gcast_delay

    if len(message.command) > 1:
        query = message.command[1].lower()
        if query.startswith("on"):
            auto_gcast_on = True
            await message.reply("Auto-gcast is now on!")
            await auto_gcast()  # Pass app as an argument
        elif query.startswith("of"):
            auto_gcast_on = False
            await message.reply("Auto-gcast is now off!")
        elif query.startswith("text"):
            auto_gcast_text = " ".join(message.command[2:])
            await message.reply("Auto-gcast text set.")
        elif query.startswith("delay"):
            auto_gcast_delay = int(message.command[2])
            await message.reply(f"Auto-gcast delay set to {auto_gcast_delay} seconds.")
        elif query.startswith("list"):
            # Handle displaying the auto-gcast text list
            await message.reply(f"Auto-gcast text: {auto_gcast_text}")
        else:
            await message.reply("Invalid query. Use '/autogcast on', '/autogcast off', '/autogcast text <text>', '/autogcast delay <delay>', or '/autogcast list'.")
    else:
        await message.reply("Please specify a query. Use '/autogcast on', '/autogcast off', '/autogcast text <text>', '/autogcast delay <delay>', or '/autogcast list'.")
