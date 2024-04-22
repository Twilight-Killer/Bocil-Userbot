from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatType

from PyroUbot import *

__MODULE__ = "logs"
__HELP__ = """
<b>『 BANTUAN UNTUK LOGS 』</b>

  <b>• PERINTAH:</b> <code>{0}logs</code> (on)
  <b>• PENJELASAN:</b> untuk mengaktifkan atau menonaktifkan channel logs

  <b>• PERINTAH:</b> <code>{0}del logs</code> 
  <b>• PENJELASAN:</b> untuk menghapus channel logs
"""

@ubot.on_message(filters.group & filters.mentioned & filters.incoming, group=4)
@ubot.on_message(
    filters.private
    & filters.incoming
    & ~filters.me
    & ~filters.bot
    & ~filters.service, group=5
)
async def send_logs(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")
    
    if not logs or not on_logs:
        return
    
    if message.chat.type == ChatType.PRIVATE:
        type = "PRIVAT"
        from_user = message.chat
        id_link = f"tg://openmessage?user_id={from_user.id}&message_id={message.id}"
    elif message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
        if not message.from_user:
            return
        type = "GRUP"
        from_user = message.from_user
        id_link = message.link
        
    rpk = f"[{from_user.first_name} {from_user.last_name or ''}](tg://user?id={from_user.id})"
    link = f"[KLIK DISINI]({id_link})"

    if message.photo:
        photo_path = await client.download_media(message.photo.file_id)
        try:
            await client.send_photo(int(logs), photo=photo_path, caption=f"ℹ️ ʟɪɴᴋ ᴘᴇsᴀɴ: {link}\n\n📌 ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇsᴀɴ ᴛᴇʀᴜsᴀɴ ᴅᴀʀɪ: {rpk}")
        except pyrogram.errors.exceptions.bad_request_400.ChatForwardsRestricted:
            await client.send_message(message.chat.id, "❌Maaf, bot tidak bisa menerima media dari grup Anda karena dibatasi❌")
    elif message.video:
        video_path = await client.download_media(message.video.file_id)
        try:
            await client.send_video(int(logs), video=video_path, caption=f"ℹ️ ʟɪɴᴋ ᴘᴇsᴀɴ: {link}\n\n📌 ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇsᴀɴ ᴛᴇʀᴜsᴀɴ ᴅᴀʀɪ: {rpk}")
        except pyrogram.errors.exceptions.bad_request_400.ChatForwardsRestricted:
            await client.send_message(message.chat.id, "❌sᴏʀʀʏ ʙʀᴏ ʟᴏɢs ɢᴜᴀ ɢᴀᴋ ʙɪsᴀ ɴᴇʀɪᴍᴀ ᴍᴇᴅɪᴀ ᴅᴀʀɪ ʟᴜ ɢᴄ ɴʏᴀ ᴅɪ ʙᴀᴛᴀsɪ❌")
    else:
        await client.send_message(
            int(logs),
            f"""
<b>📩 Ada pesan masuk</b>
    <b>•> Tipe pesan:</b> <code>{type}</code>
    <b>•> Link pesan:</b> {link}
    <b>•> Pesan:</b> {message.text}
    
<b>⤵️ Dibawah ini adalah pesan terusan dari: {rpk}</b>
""",
        )
      
@PY.UBOT("logs")
async def set_logs(client, message: Message):
    if len(message.command) < 2:
        return await message.reply(
            "ʜᴀʀᴀᴘ ʙᴀᴄᴀ ᴍᴇɴᴜ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴄᴀʀᴀ ᴘᴇɴɢɢụ"
        )

    query = {"on": True}
    command = message.command[1].lower()

    if command not in query:
        return await message.reply("ᴏᴘsɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ʜᴀʀᴀᴘ ɢᴜɴᴀᴋᴀɴ 'on'.")

    value = query[command]

    vars = await get_vars(client.me.id, "ID_LOGS")

    if not vars:
        logs = await create_logs(client)
        await set_vars(client.me.id, "ID_LOGS", logs)

    await set_vars(client.me.id, "ON_LOGS", value)
    return await message.reply(
        f"<b>✅ <code>LOGS</code> ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴛɪɴɢ ᴋᴇ:</b> <code>{value}</code>"
    )

@PY.UBOT("del logs")
async def del_logs(client, message: Message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    if not logs:
        return await message.reply("Logs belum diatur.")

    try:
        await client.leave_chat(int(logs))
        await set_vars(client.me.id, "ID_LOGS", None)
        await set_vars(client.me.id, "ON_LOGS", False)
        return await message.reply("ʟᴏɢs ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs❌")
    except Exception as e:
        return await message.reply(f"Gagal menghapus logs: {e}")

async def create_logs(client):
    url = wget.download("https://graph.org/file/5b61f029143eadf42020e.jpg")
    logs = await client.create_channel(f"logs: {client.me.username}")
    await client.set_chat_photo(
        logs.id,
        photo=url,
    )
    return logs.id
