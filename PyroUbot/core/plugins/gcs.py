import asyncio
from gc import get_objects

from pyrogram.errors import FloodWait
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

from PyroUbot import *


async def is_premium_user(client):
    return client.me.is_premium


async def get_message_content(message):
    if message.reply_to_message:
        return message.reply_to_message
    else:
        return message.text


async def broadcast_group_cmd(client, message):
    proses_emoji = "<emoji id=5971865795582495562>🔺</emoji>"
    success_emoji = "<emoji id=5021905410089550576>✅</emoji>"
    failure_emoji = "<emoji id=5019523782004441717>❌</emoji>"
    selesai_emoji = "<emoji id=5895735846698487922>🌐</emoji>"
    reply_emoji = "<emoji id=6226230182806554486>🚫</emoji>"

    processing_msg = (
        f"{proses_emoji} Sedang memproses, mohon bersabar..."
        if await is_premium_user(client)
        else "Sedang memproses, mohon bersabar..."
    )
    msg = await message.reply_text(processing_msg, quote=True)

    send = await get_message_content(message)
    if not send:
        return await msg.edit_text(
            f"{reply_emoji} Mohon balas sesuatu atau ketik sesuatu"
            if await is_premium_user(client)
            else "🔁 Mohon balas sesuatu atau ketik sesuatu"
        )

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
            try:
                if message.reply_to_message:
                    await send.copy(chat_id)
                else:
                    await client.send_message(chat_id, send)
                done += 1
            except Exception as ex:
                print(f"Failed to send message to {chat_id} due to {ex}")
                failed += 1
        except Exception as ex:
            print(f"Failed to send message to {chat_id} due to {ex}")
            failed += 1

    await msg.delete()
    return await message.reply_text(
        (
            f"{selesai_emoji} Pesan broadcast selesai\n{success_emoji} Berhasil ke: {done} grup\n{failure_emoji} Gagal ke: {failed} grup"
            if await is_premium_user(client)
            else f"❏ Pesan broadcast selesai\n├ Berhasil ke: {done} grup\n╰ Gagal ke: {failed} grup"
        ),
        quote=True,
    )


async def broadcast_users_cmd(client, message):
    processing_msg = (
        "Sedang memproses, mohon bersabar..."
        if await is_premium_user(client)
        else "Sedang memproses, mohon bersabar..."
    )
    msg = await message.reply_text(processing_msg, quote=True)

    send = await get_message_content(message)
    if not send:
        return await msg.edit_text(
            "Mohon balas sesuatu atau ketik sesuatu"
            if await is_premium_user(client)
            else "Mohon balas sesuatu atau ketik sesuatu"
        )

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
            try:
                if message.reply_to_message:
                    await send.copy(chat_id)
                else:
                    await client.send_message(chat_id, send)
                done += 1
            except Exception as ex:
                print(f"Failed to send message to {chat_id} due to {ex}")
                failed += 1
        except Exception as ex:
            print(f"Failed to send message to {chat_id} due to {ex}")
            failed += 1

    await msg.delete()
    return await message.reply_text(
        (
            f"Pesan broadcast selesai\n✅ Berhasil ke: {done} users\n❌ Gagal ke: {failed} users"
            if await is_premium_user(client)
            else f"❏ Pesan broadcast selesai\n├ Berhasil ke: {done} users\n╰ Gagal ke: {failed} users"
        ),
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
            return await message.reply_text(str(error))
        else:
            try:
                return await message.reply_to_message.copy(chat_id)
            except Exception as t:
                return await message.reply_text(str(t))
    else:
        if len(message.command) < 3:
            return await message.reply_text("Ketik yang benar")
        chat_id, chat_text = message.text.split(None, 2)[1:]
        try:
            return await client.send_message(chat_id, chat_text)
        except Exception as t:
            return await message.reply_text(str(t))


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
