from pyrogram.types import Message, ChatPermissions
from pyrogram.enums import ChatType


from PyroUbot import *


__MODULE__ = "bluser"
__HELP__ = """
<b>『 bantuan bluser 』</b>

  <b>• perintah:</b> <code>{0}ler</code>
  <b>• penjelasan:</b> taypingan hilang

  <b>• penjelasan:</b> <code>{0}unler</code> [reply user to media]
  <b>• perintah:</b> hapus dari daftar ler

  <b>• perintah:</b> <code>{0}listler</code> [username/chanel/group]
  <b>• penjelasan:</b> cek daftar ler
"""


@PY.UBOT("ler")
async def blacklist_user(client: Client, message: Message):
    bot_id = client.me.id
    if message.chat.type in {ChatType.SUPERGROUP, ChatType.GROUP}:
        if message.reply_to_message and message.reply_to_message.from_user:
            user_id = message.reply_to_message.from_user.id
            await add_to_blacklist(bot_id, user_id)
            await message.reply_text("Pengguna berhasil ditambahkan ke daftar dor.")
        elif len(message.command) > 1:
            username = message.command[1]
            try:
                user = await client.get_users(username)
                user_id = user.id
                await add_to_blacklist(bot_id, user_id)
                await message.reply_text("Pengguna berhasil ditambahkan ke daftar dor.")
            except Exception as e:
                await message.reply_text(f"Gagal menemukan pengguna: {str(e)}")
        else:
            await message.reply_text("Mohon balas pesan pengguna yang ingin ditambahkan ke daftar dor atau sebutkan username.")
    else:
        await message.reply_text("Perintah ini hanya dapat digunakan dalam grup.")

@PY.UBOT("unler")
async def unblacklist_user(client: Client, message: Message):
    bot_id = client.me.id
    if message.chat.type in {ChatType.SUPERGROUP, ChatType.GROUP}:
        if message.reply_to_message and message.reply_to_message.from_user:
            user_id = message.reply_to_message.from_user.id
            await remove_from_blacklist(bot_id, user_id)
            await message.reply_text("Pengguna berhasil dihapus dari daftar dor.")
        elif len(message.command) > 1:
            username = message.command[1]
            try:
                user = await client.get_users(username)
                user_id = user.id
                await remove_from_blacklist(bot_id, user_id)
                await message.reply_text("Pengguna berhasil dihapus dari daftar dor.")
            except Exception as e:
                await message.reply_text(f"Gagal menemukan pengguna: {str(e)}")
        else:
            await message.reply_text("Mohon balas pesan pengguna yang ingin dihapus dari daftar dor atau sebutkan username.")
    else:
        await message.reply_text("Perintah ini hanya dapat digunakan dalam grup.")

@PY.UBOT("listler")
async def list_blacklisted_users(client: Client, message: Message):
    bot_id = client.me.id
    if message.chat.type in {ChatType.SUPERGROUP, ChatType.GROUP}:
        blacklisted_users = await get_blacklisted_users(bot_id)
        if blacklisted_users:
            users_info = await client.get_users(blacklisted_users)
            users_list = "\n".join([f"{i+1}. {user.first_name} ({user.id})" for i, user in enumerate(users_info)])
            await message.reply_text(f"Daftar pengguna dalam daftar dor:\n\n{users_list}")
        else:
            await message.reply_text("Daftar dor kosong.")
    else:
        await message.reply_text("Perintah ini hanya dapat digunakan dalam grup.")

@ubot.on_message(filters.group)
async def delete_blacklisted_users_message(client, message):
    bot_id = client.me.id
    blacklisted_users = await get_blacklisted_users(bot_id)
    if message.from_user and message.from_user.id in blacklisted_users:
        await message.delete()
