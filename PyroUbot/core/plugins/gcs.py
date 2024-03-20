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

# Data auto_gcast
auto_gcast_data = {
    "status": False,    # ON/OFF
    "text": "",         # TEXT
    "delay": 0,         # DELAY
    "limit": False,     # LIMIT
    "failed_text": "",  # TEXT yang gagal terkirim
    "success_text": "", # TEXT yang berhasil terkirim
    "texts": []         # Daftar teks yang akan dikirim
}

# Fungsi untuk mengaktifkan/menonaktifkan auto_gcast
def toggle_auto_gcast(query, value):
    global auto_gcast_data
    if query.upper() == "ON":
        auto_gcast_data["status"] = True
    elif query.upper() == "OFF":
        auto_gcast_data["status"] = False
    value["text"] = f"Auto-GCAST sekarang {'aktif' if auto_gcast_data['status'] else 'non-aktif'}"
    return value

def set_text(query, value):
    global auto_gcast_data
    auto_gcast_data["text"] = value
    return f"Teks Auto-GCAST diatur menjadi: {value}"

# Fungsi untuk mengatur delay auto_gcast
def set_delay(query, value):
    global auto_gcast_data
    try:
        auto_gcast_data["delay"] = int(query)
        value["text"] = f"Delay Auto-GCAST diatur menjadi: {query} detik"
    except ValueError:
        value["text"] = "Silakan masukkan angka untuk delay"
    return value

# Fungsi untuk mengaktifkan/menonaktifkan limit auto_gcast
def toggle_limit(query, value):
    global auto_gcast_data
    if query.upper() == "ON":
        auto_gcast_data["limit"] = True
    elif query.upper() == "OFF":
        auto_gcast_data["limit"] = False
    value["text"] = f"Limit Auto-GCAST sekarang {'aktif' if auto_gcast_data['limit'] else 'non-aktif'}"
    return value

# Fungsi untuk menambahkan teks ke daftar teks
def add_text(query, value):
    global auto_gcast_data
    auto_gcast_data["texts"].append(query)
    value["text"] = f"Teks '{query}' telah ditambahkan ke daftar teks"
    return value

# Fungsi untuk menampilkan daftar teks yang akan dikirim
def list_texts(query, value):
    global auto_gcast_data
    texts = "\n".join(auto_gcast_data["texts"])
    if not texts:
        value["text"] = "Daftar teks kosong"
    else:
        value["text"] = f"Daftar teks yang akan dikirim:\n{texts}"
    return value


def add_to_all_groups(func):
    async def wrapper(client, message):
        success_count = 0
        fail_count = 0
        for chat in client.iter_dialogs():
            if chat.chat.type in ["group", "supergroup"]:
                try:
                    await func(client, chat.chat.id, message)
                    success_count += 1
                except Exception as e:
                    fail_count += 1
        return success_count, fail_count
    return wrapper

async def send_to_all_groups(client, chat_id, message):
    await client.send_message(chat_id, message)

async def auto_gcast_command(client, message):
    global auto_gcast_data
    split = message.text.split(maxsplit=2)
    if len(split) != 3:
        await message.reply("Format perintah salah. Gunakan: .auto_gcast <query> - <value>")
        return
    query, value = split[1], split[2]
    if query.upper() == "ON" or query.upper() == "OFF":
        value = toggle_auto_gcast(query, value)
    elif query.upper() == "TEXT":
    result = set_text(query, value)
    value = {"text": result}
    elif query.upper() == "DELAY":
        result = set_delay(value)
        value = {"text": result}
    elif query.upper() == "LIMIT":
        value = toggle_limit(query, value)
    elif query.upper() == "ADD":
        value = add_text(value)
    elif query.upper() == "LIST":
        value = list_texts(value)
    
    success_count, fail_count = await send_to_all_groups(client, message.chat.id, auto_gcast_data["text"])  # Kirim pesan ke semua grup atau supergrup
    value["text"] += f"\n\nBerhasil mengirim ke {success_count} grup/supergroup" if success_count > 0 else ""
    value["text"] += f"\nGagal mengirim ke {fail_count} grup/supergroup" if fail_count > 0 else ""
    
    await message.reply(value["text"])
