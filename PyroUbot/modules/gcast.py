import asyncio
from pyrogram.types import Message
from pyrogram.errors import FloodWait, Forbidden
from datetime import datetime, timedelta
import pytz
import random
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from PyroUbot import*

__MODULE__ = "gcast"
__HELP__ = """
<b>『 bantuan gcast 』</b>

  <b>• perintah:</b> <code>{0}ucast</code> [text/reply to text/media]
  <b>• penjelasan:</b> mengirim pesan ke chat 

  <b>• perintah:</b> <code>{0}gcast</code> [text/reply to text/media]
  <b>• penjelasan:</b> mengirim pesan ke group 

  <b>• perintah:</b> <code>{0}send</code> [userid/username to reply/text]
  <b>• penjelasan:</b> mengirim pesan ke group channel chat

    <b>• perintah:</b> auto_gcast (qury) - (value)
      <b>•> query & value:</b>
        <b>on/off:</b> untuk aktifkan dan nonaktifkan auto_gcast
        <b>text - kata-kata/reply_text:<b> menambahkan kata kata ke database
        <b>delay - angka:</b> merubah delay auto gcast
        <b>limit - on/off:</b> aktif/non-aktif untuk cek limit 15 menit sekali
  <b>• penjelasan:</b> mengerim pesan gcast otomatis 

  <b>• perintah:</b> <code>{0}gban</ᴄᴏᴅᴇ> [userid/username to reply/user]
  <b>• penjelasan:</b> banned pengguna 

  <b>• perintah:</b> <code>{0}ungban</code> [user_id/username to reply/user]
  <b>• penjelasan:</b> unban pengguna 
"""


@PY.UBOT("gcast")
async def _(client, message):
    await broadcast_group_cmd(client, message)


@PY.UBOT("ucast")
async def _(client, message):
    await broadcast_users_cmd(client, message)


@PY.BOT("send")
@PY.UBOT("send")
async def _(client, message):
    await send_msg_cmd(client, message)


@PY.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)


@PY.UBOT("gban")
async def _(client, message):
    await global_banned(client, message)


@PY.UBOT("ungban")
async def _(client, message):
    await global_unbanned(client, message)


AG = []
LT = []

WIB = pytz.timezone('Asia/Jakarta')

@PY.UBOT("auto_gcast")
async def auto_gcast(client, message):
    msg = await message.reply("Sedang memproses...", quote=True)
    type, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT") or []

    if type == "on":
        if client.me.id not in AG:
            AG.append(client.me.id)
            await start_auto_gcast(client, msg, value, auto_text_vars)
        else:
            return await msg.delete()
    elif type == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit("Auto gcast telah dinonaktifkan.")
        else:
            return await msg.delete()
    elif type == "text":
        if not value:
            return await msg.edit("Harap masukkan teks untuk disimpan sebagai teks auto gcast.")
        await add_auto_text(client, value)
        return await msg.edit("Auto gcast text: Berhasil disimpan.")
    elif type == "delay":
        await set_vars(client.me.id, "DELAY_GCAST", value)
        return await msg.edit(f"Auto gcast delay: Berhasil disetting {value} menit.")
    elif type == "remove":
        await handle_text_removal(client, msg, value, auto_text_vars)
    elif type == "list":
        await list_auto_texts(client, msg, auto_text_vars)
    elif type == "limit":
        await handle_limit_check(client, msg, value)
    else:
        return await msg.edit("Query yang dimasukkan salah.")

async def start_auto_gcast(client, msg, value, auto_text_vars):
    try:
        if value:
            try:
                send_time = datetime.strptime(value, "%H:%M").time()
                await schedule_gcast(client, msg, send_time, auto_text_vars)
            except ValueError:
                return await msg.edit("Format waktu tidak valid. Gunakan format HH:MM.")
        else:
            await msg.edit("Auto gcast diaktifkan.")
            await perform_auto_gcast(client, msg, auto_text_vars)
    except Exception as e:
        logger.error(f"Error in start_auto_gcast: {e}")
        AG.remove(client.me.id)
        await msg.edit(f"Error saat memulai auto gcast: {e}")

async def schedule_gcast(client, msg, send_time, auto_text_vars):
    now = datetime.now(WIB)
    target_time = WIB.localize(datetime.combine(now.date(), send_time))
    if target_time < now:
        target_time += timedelta(days=1)
    wait_time = (target_time - now).total_seconds()
    await msg.edit(f"Auto gcast diaktifkan. Akan mengirim pesan pada {send_time} WIB.")
    await asyncio.sleep(wait_time)
    await perform_auto_gcast(client, msg, auto_text_vars)

async def perform_auto_gcast(client, msg, auto_text_vars):
    done = 0
    while client.me.id in AG:
        delay = int(await get_vars(client.me.id, "DELAY_GCAST") or 1)
        blacklist = await get_chat(client.me.id) or []
        txt = random.choice(auto_text_vars)
        group, limit_detected = 0, False

        async for dialog in client.get_dialogs():
            if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP) and dialog.chat.id not in blacklist:
                try:
                    await asyncio.sleep(1)
                    await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(1000))}")
                    group += 1
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except Forbidden:
                    continue
                except Exception as e:
                    logger.error(f"Unexpected error in perform_auto_gcast: {e}")
                    limit_detected = True
                    continue

        done += 1
        await send_status_message(client, msg, done, group, limit_detected, delay)
        await asyncio.sleep(60 * delay)

async def send_status_message(client, msg, done, group, limit_detected, delay):
    status_message = (
        f"Auto gcast putaran {done} berhasil dan terkirim ke: {group} grup."
        f"\n\nMenunggu {delay} menit lagi untuk mengulang mengirim pesan."
    )
    await msg.reply(status_message, quote=True)

async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)

async def handle_text_removal(client, msg, value, auto_text_vars):
    if not value:
        return await msg.edit("Harap masukkan angka untuk menghapus list teks.")
    if value == "all":
        await set_vars(client.me.id, "AUTO_TEXT", [])
        return await msg.edit("Semua teks berhasil dihapus.")
    try:
        value = int(value) - 1
        auto_text_vars.pop(value)
        await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
        return await msg.edit(f"Auto gcast remove: Teks ke {value+1} berhasil dihapus.\n\nKetik: <code>{message.text.split()[0]} list</code>, untuk mengecek apakah sudah terhapus.")
    except Exception as error:
        return await msg.edit(str(error))

async def list_auto_texts(client, msg, auto_text_vars):
    if not auto_text_vars:
        return await msg.edit("Auto gcast teks kosong.")
    txt = "Daftar auto gcast teks\n\n"
    for num, x in enumerate(auto_text_vars, 1):
        txt += f"{num}: {x}\n\n"
    txt += f"\nUntuk menghapus teks ketik: <code>{msg.text.split()[0]} remove angka/all</code>"
    return await msg.edit(txt)

async def handle_limit_check(client, msg, value):
    if value == "off":
        if client.me.id in LT:
            LT.remove(client.me.id)
            return await msg.edit("Auto cek limit dinonaktifkan.")
        else:
            return await msg.delete()
    elif value == "on":
        if client.me.id not in LT:
            LT.append(client.me.id)
            await msg.edit("Auto cek limit dimulai.")
            while client.me.id in LT:
                await limit_cmd(client, msg)
                await asyncio.sleep(1200)
        else:
            return await msg.delete()
    else:
        return await msg.edit("Harap masukkan value on/off untuk menggunakan perintah ini.")

async def limit_cmd(client, message):
    try:
        await client.unblock_user("SpamBot")
        bot_info = await client.resolve_peer("SpamBot")
        response = await client.invoke(
            StartBot(
                bot=bot_info,
                peer=bot_info,
                random_id=client.rnd_id(),
                start_param="start",
            )
        )
        await asyncio.sleep(1)
        status = await client.get_messages("SpamBot", response.updates[1].message.id + 1)
        await status.copy(message.chat.id, reply_to_message_id=message.id)
        await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
    except Exception as e:
        logger.error(f"Error in limit check: {e}")

def extract_type_and_text(message):
    args = message.text.split(None, 2)
    if len(args) < 2:
        return None, None

    type = args[1]
    msg = (
        message.reply_to_message.text
        if message.reply_to_message
        else args[2]
        if len(args) > 2
        else None
    )
    return type, msg
