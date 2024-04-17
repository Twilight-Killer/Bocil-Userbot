import asyncio
from pyrogram.enums import UserStatus

from PyroUbot import *


async def invite_cmd(client, message):
    mg = await message.reply("<b>Menambahkan pengguna!</b>")
    user_s_to_add = message.text.split(" ", 1)
    if len(user_s_to_add) < 2:
        return await mg.delete()
    user_s_to_add = user_s_to_add[1]
    if not user_s_to_add:
        await mg.edit(
            "<b>Beri saya pengguna untuk ditambahkan! Periksa menu bantuan untuk info lebih lanjut!</b>"
        )
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except Exception as e:
        return await mg.edit(f"{e}")
    await mg.edit(f"<b>Berhasil ditambahkan {len(user_list)} ke grup ini</b>")

invite_id = []

async def inviteall_cmd(client, message):
    if len(message.command) < 3:
        return await message.reply("<b>Usage:</b> <code>/inviteall {chat_id} {delay}</code>")

    chat_id = message.command[1]
    try:
        delay = int(message.command[2])
    except ValueError:
        return await message.reply("Delay harus berupa bilangan bulat.")

    try:
        chat = await client.get_chat(chat_id)
    except Exception as e:
        return await message.reply(f"Error: {e}")

    if message.chat.id in invite_id:
        return await message.reply("Invitation process is already running, please try again later or use /cancel")

    invite_id.append(message.chat.id)
    tm = await message.reply(f"Inviting members from {chat.title}...")

    done = 0
    failed = 0
    async for member in client.iter_chat_members(chat.id):
        if member.user.status in [
            UserStatus.ONLINE,
            UserStatus.OFFLINE,
            UserStatus.RECENTLY,
            UserStatus.LAST_WEEK,
        ]:
            try:
                await client.add_chat_members(message.chat.id, member.user.id)
                done += 1
            except Exception as e:
                failed += 1
            await asyncio.sleep(delay)

    invite_id.remove(message.chat.id)
    await tm.edit(f"Invitation completed.\n\nSuccessfully invited: {done} members\nFailed to invite: {failed} members")

async def cancel_cmd(client, message):
    if message.chat.id not in invite_id:
        return await message.reply_text(
            "Tidak ada perintah inviteall yang sedang berjalan di grup ini."
        )
    try:
        invite_id.remove(message.chat.id)
        await message.reply_text("Proses inviteall berhasil dibatalkan.")
    except Exception as e:
        await message.reply_text(e)
