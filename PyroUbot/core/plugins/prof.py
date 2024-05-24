from pyrogram import Client, filters
from pyrogram.types import Message

from PyroUbot import *


async def set_bio(client: Client, message: Message):
    text = message.text.split(maxsplit=1)
    if len(text) > 1:
        new_bio = text[1]
        try:
            await client.set_user_bio(new_bio)
            await message.reply_text("Bio berhasil diubah!")
        except Exception as e:
            await message.reply_text(f"Gagal mengubah bio: {e}")
    else:
        await message.reply_text("Mohon sertakan teks untuk bio.")


async def set_name(client: Client, message: Message):
    text = message.text.split(maxsplit=1)
    if len(text) > 1:
        new_name = text[1]
        try:
            await client.update_profile(first_name=new_name)
            await message.reply_text("Nama berhasil diubah!")
        except Exception as e:
            await message.reply_text(f"Gagal mengubah nama: {e}")
    else:
        await message.reply_text("Mohon sertakan teks untuk nama baru.")


async def block_user(client: Client, message: Message):
    text = message.text.split()
    if len(text) == 2 and text[1].isdigit():
        user_id = int(text[1])
        try:
            await client.block_user(user_id)
            await message.reply_text("Pengguna berhasil diblokir!")
        except Exception as e:
            await message.reply_text(f"Gagal memblokir pengguna: {e}")
    elif message.reply_to_message and message.reply_to_message.from_user:
        try:
            await client.block_user(message.reply_to_message.from_user.id)
            await message.reply_text("Pengguna berhasil diblokir!")
        except Exception as e:
            await message.reply_text(f"Gagal memblokir pengguna: {e}")
    else:
        await message.reply_text("Mohon balas pesan pengguna yang ingin Anda blokir atau sertakan ID pengguna.")


async def unblock_user(client: Client, message: Message):
    text = message.text.split()
    if len(text) == 2 and text[1].isdigit():
        user_id = int(text[1])
        try:
            await client.unblock_user(user_id)
            await message.reply_text("Pengguna berhasil dibuka blokir!")
        except Exception as e:
            await message.reply_text(f"Gagal membuka blokir pengguna: {e}")
    elif message.reply_to_message and message.reply_to_message.from_user:
        try:
            await client.unblock_user(message.reply_to_message.from_user.id)
            await message.reply_text("Pengguna berhasil dibuka blokir!")
        except Exception as e:
            await message.reply_text(f"Gagal membuka blokir pengguna: {e}")
    else:
        await message.reply_text("Mohon balas pesan pengguna yang ingin Anda buka blokir atau sertakan ID pengguna.")


