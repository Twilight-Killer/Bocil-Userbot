import asyncio

from gc import get_objects
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from pyrogram.errors import RPCError, FloodWait, ChatWriteForbidden


from PyroUbot import*

async def broadcast_group_cmd(client, message):
    emojis = {
        "processing": "<emoji id=5971865795582495562>🔺</emoji>",
        "success": "<emoji id=5021905410089550576>✅</emoji>",
        "failure": "<emoji id=5019523782004441717>❌</emoji>",
        "done": "<emoji id=5895735846698487922>🌐</emoji>",
        "reply": "<emoji id=6226230182806554486>🚫</emoji>"
    }

    processing_msg = f"{emojis['processing']} Sedang memproses, mohon bersabar..." if client.me.is_premium else "Sedang memproses, mohon bersabar..."
    msg = await message.reply(processing_msg, quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit(f"{emojis['reply']} Mohon balas sesuatu atau ketik sesuatu" if client.me.is_premium else "🔁 Mohon balas sesuatu atau ketik sesuatu")

    chats = await get_global_id(client, "group")
    blacklist = await get_chat(client.me.id)

    done, failed = 0, 0
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
            except (ChatWriteForbidden, RPCError) as e:
                failed += 1
                print(f"Error sending to {chat_id}: {e}")
        except ChatWriteForbidden:
            failed += 1
            print(f"Tidak memiliki hak untuk mengirim pesan di obrolan {chat_id}")
        except RPCError as e:
            failed += 1
            if e.MESSAGE == "USER_BANNED_IN_CHANNEL":
                print(f"Error: Anda dibatasi dari mengirim pesan di obrolan {chat_id}")
            elif e.MESSAGE == "SLOWMODE_WAIT_X":
                print(f"Error: Waktu tunggu mode lambat diperlukan di obrolan {chat_id}")
            else:
                print(f"RPCError saat mengirim ke {chat_id}: {e}")
        except Exception as ex:
            failed += 1
            print(f"Exception saat mengirim ke {chat_id}: {ex}")

    await msg.delete()
    return await message.reply(
        f"{emojis['done']} Pesan broadcast selesai\n{emojis['success']} Berhasil ke: {done} grup\n{emojis['failure']} Gagal ke: {failed} grup" if client.me.is_premium else f"❏ Pesan broadcast selesai\n├ Berhasil ke: {done} grup\n╰ Gagal ke: {failed} grup",
        quote=True
            )

async def broadcast_users_cmd(client, message):
    msg = await message.reply("Sedang memproses, mohon bersabar..." if client.me.is_premium else "Sedang memproses, mohon bersabar...", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("Mohon balas sesuatu atau ketik sesuatu" if client.me.is_premium else "Mohon balas sesuatu atau ketik sesuatu")

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
            print(f"Message sent to {chat_id}")
        except FloodWait as e:
            print(f"FloodWait for {e.value} seconds while sending to {chat_id}")
            await asyncio.sleep(e.value)
            try:
                if message.reply_to_message:
                    await send.copy(chat_id)
                else:
                    await client.send_message(chat_id, send)
                done += 1
                print(f"Message sent to {chat_id} after FloodWait")
            except (ChatWriteForbidden, RPCError) as e:
                failed += 1
                print(f"Error during FloodWait retry for {chat_id}: {e}")
        except ChatWriteForbidden as e:
            failed += 1
            print(f"Error: No rights to send messages in chat {chat_id}")
        except RPCError as e:
            failed += 1
            if e.MESSAGE == "USER_BANNED_IN_CHANNEL":
                print(f"Error: You are banned from sending messages in chat {chat_id}")
            elif e.MESSAGE == "SLOWMODE_WAIT_X":
                print(f"Error: Slow mode wait required in chat {chat_id}")
            else:
                print(f"RPCError while sending to {chat_id}: {e}")
        except Exception as ex:
            failed += 1
            print(f"Exception while sending to {chat_id}: {ex}")

    await msg.delete()
    return await message.reply(
        f"Pesan broadcast selesai\n✅ Berhasil ke: {done} users\n❌ Gagal ke: {failed} users" if client.me.is_premium else f"❏ Pesan broadcast selesai\n├ Berhasil ke: {done} users\n╰ Gagal ke: {failed} users",
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
