import asyncio

from gc import get_objects
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from pyrogram.errors import FloodWait

from PyroUbot import*

# Emoji IDs
proses_emoji = "<emoji id=5971865795582495562>🔺</emoji>"
success_emoji = "<emoji id=5021905410089550576>✅</emoji>"
failure_emoji = "<emoji id=5019523782004441717>❌</emoji>"
selesai_emoji = "<emoji id=5895735846698487922>🌐</emoji>"
reply_emoji = "<emoji id=6226230182806554486>🚫</emoji>"

async def broadcast_group_cmd(client, message):

    processing_msg = f"{proses_emoji} Sedang memproses, mohon bersabar..."
    msg = await message.reply(processing_msg, quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit(f"{reply_emoji} Mohon balas sesuatu atau ketik sesuatu")

    chats = await get_global_id(client, "group")
    blacklist = await get_chat(client.me.id)

    done = 0
    failed = 0
    inaccessible = 0
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
        except ChannelPrivate:
            inaccessible += 1
        except Exception:
            failed += 1
            # print(f"Error: {e}")  # Logging error for debugging

    await msg.delete()
    return await message.reply(
        f"{selesai_emoji} Pesan broadcast selesai\n{success_emoji} Berhasil ke: {done} grup\n{failure_emoji} Gagal ke: {failed} grup\n{reply_emoji} Tidak dapat diakses: {inaccessible} grup",
        quote=True,
    )

async def broadcast_users_cmd(client, message):
    msg = await message.reply("Sedang memproses, mohon bersabar...", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("Mohon balas sesuatu atau ketik sesuatu")

    chats = await get_global_id(client, "users")

    done = 0
    failed = 0
    inaccessible = 0
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
        except ChannelPrivate:
            inaccessible += 1
        except Exception as e:
            failed += 1
            # print(f"Error: {e}")  # Logging error for debugging

    await msg.delete()
    return await message.reply(
        f"Pesan broadcast selesai\n✅ Berhasil ke: {done} users\n❌ Gagal ke: {failed} users\n🚫 Tidak dapat diakses: {inaccessible} users",
        quote=True,
    )

async def send_msg_cmd(client, message):
    if message.reply_to_message:
        chat_id = (
            message.chat.id if len(message.command) < 2 else message.text.split()[1]
        )
        try:
            me = await client.get_me()
            if me.id != bot.me.id:
                if message.reply_to_message.reply_markup:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"get_send {id(message)}"
                    )
                    return await client.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
        except Exception as error:
            return await message.reply(str(error))
        else:
            try:
                return await message.reply_to_message.copy(chat_id)
            except Exception as t:
                return await message.reply(str(t))
    else:
        if len(message.command) < 3:
            return await message.reply("Ketik yang benar")
        chat_id, chat_text = message.text.split(None, 2)[1:]
        try:
            return await client.send_message(chat_id, chat_text)
        except Exception as t:
            return await message.reply(str(t))

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
