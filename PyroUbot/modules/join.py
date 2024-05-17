from pyrogram.enums import ChatType
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

# Import bot Anda dari modul yang sesuai
from PyroUbot import *  # Pastikan PY.UBOT diimpor dengan benar dari modul Anda

# Asumsikan BLACKLIST_CHAT didefinisikan di suatu tempat dalam modul ubot Anda
BLACKLIST_CHAT = []  # Ganti dengan ID chat yang sebenarnya


__MODULE__ = "join"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀғᴋ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}kickme</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> keluar dari group

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}join</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> join group melalui username

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}leave</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> keluar dari group melalui username

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}leaveallgc</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> keluar dari semua gc

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}leaveallch</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> keluar dari semua ch

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}leaveallmute</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> keluar dari group yang akun lu di miut  
"""


@PY.UBOT("kickme")
async def kickme(client, message: Message):
    if message.chat.id in BLACKLIST_CHAT:
        await message.reply("Dilarang menggunakan perintah ini disini.")
        return
    user = await client.get_me()  # Get the client user info
    await message.reply(f"{user.first_name} Aku depresi.")
    await client.leave_chat(message.chat.id)


@PY.UBOT("join")
async def join(client, message: Message):
    mam = message.command[1] if len(message.command) > 1 else message.chat.id
    yaa = await message.reply("Processing...")
    try:
        await client.join_chat(mam)
        await xxnx.edit(f"Berhasil bergabung ke: `{mam}`")
    except Exception as ex:
        await xxnx.edit(f"ERROR:\n\n{str(ex)}")


@PY.UBOT("leave")
async def leave(client, message: Message):
    mam = message.command[1] if len(message.command) > 1 else message.chat.id
    yaa = await message.reply("Processing...")
    if message.chat.id in BLACKLIST_CHAT:
        return await yaa.edit("Dilarang menggunakan perintah ini disini.")
    user = await client.get_me()  
    try:
        await client.leave_chat(mam)
        await yaa.edit_text(f"{user.first_name} Aku depresi.")
    except Exception as ex:
        await xxnx.edit_text(f"ERROR:\n\n{str(ex)}")


@PY.UBOT("leaveallgc")
async def leave_all_groups(client, message: Message):
    mam = await message.reply("Proses Pengeluaran Global Grup...")
    cil = 0
    mek = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except Exception:
                er += 1
    await mam.edit(f"Berhasil keluar dari {mek} grup, Gagal keluar dari {cil} grup.")


@PY.UBOT("leaveallch")
async def leave_all_channels(client, message: Message):
    mam = await message.reply("Proses Pengeluaran Global Channel...")
    cil = 0
    mek = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.CHANNEL:
            chat = dialog.chat.id
            try:
                mek += 1
                await client.leave_chat(chat)
            except Exception:
                cil += 1
    await mam.edit(f"Berhasil keluar dari {mek} channel, Gagal keluar dari {cil} channel.")

@PY.UBOT("leaveallmute")
async def leave_all_muted_groups(client, message: Message):
    mam = await message.reply("Proses Pengeluaran Grup yang Dimute...")
    cil = 0
    mek = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, client.me.id)
                if member.status == ChatMemberStatus.RESTRICTED and member.is_member and member.permissions.can_send_messages is False:
                    try:
                        mek += 1
                        await client.leave_chat(chat)
                    except Exception:
                        cil += 1
            except UserNotParticipant:
                # Jika bot bukan peserta, tetap mencoba keluar dari grup
                try:
                    mek += 1
                    await client.leave_chat(chat)
                except Exception:
                    cil += 1
    await mam.edit(f"Berhasil keluar dari {mek} grup yang dimute, Gagal keluar dari {cil} grup.")
