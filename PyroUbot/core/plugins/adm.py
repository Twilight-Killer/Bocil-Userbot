import asyncio
from pyrogram.types import ChatPermissions
from PyroUbot import *


async def admin_kick(client, message):
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text("Saya tidak dapat menemukan pengguna itu.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text("Aku tidak bisa mendatangkan diriku sendiri, aku bisa pergi jika kamu mau.")
    if user_id == OWNER_ID:
        return await message.reply_text("Anda tidak bisa menendang anggota ini")
    if user_id in (await list_admins(message)):
        return await message.reply_text("Saya tidak bisa menendang admin, anda tahu aturannya, saya juga.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    msg = f"<b>👤 Ditendang:</b> {mention}\n<b>👑 Admin:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>💬 Alasan:</b> {reason}"
    try:
        if message.command[0] == "dkick":
            await message.reply_to_message.delete()
        await message.chat.kick_member(user_id)
        await message.reply(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except Exception as error:
        await message.reply(error)


async def admin_ban(client, message):
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text("Saya tidak dapat menemukan anggota itu.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text("Aku tidak bisa membanned diriku sendiri, aku bisa pergi jika kamu mau.")
    if user_id == OWNER_ID:
        return await message.reply_text("Anda tidak bisa membanned anggota ini")
    if user_id in (await list_admins(message)):
        return await message.reply_text("Anda tidak bisa membanned anggota ini")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    msg = f"<b>👤 Dibanned:</b> {mention}\n<b>👑 Admin:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>💬 Alasan:</b> {reason}"
    try:
        if message.command[0] == "dban":
            await message.reply_to_message.delete()
        await message.chat.kick_member(user_id)
        await message.reply(msg)
    except Exception as error:
        await message.reply(error)


async def admin_mute(client, message):
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text("Saya tidak dapat menemukan anggota itu.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text("Aku tidak bisa membisukan diriku sendiri, aku bisa pergi jika kamu mau.")
    if user_id == OWNER_ID:
        return await message.reply_text("Anda tidak bisa membisukan anggota ini")
    if user_id in (await list_admins(message)):
        return await message.reply_text("Saya tidak bisa membisukan admin, anda tahu aturannya, saya juga.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    msg = f"<b>👤 Membisukan:</b> {mention}\n<b>👑 Admin:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>💬 Alasan:</b> {reason}"
    try:
        if message.command[0] == "dmute":
            await message.reply_to_message.delete()
        await message.chat.restrict_member(user_id, ChatPermissions())
        await message.reply(msg)
    except Exception as error:
        await message.reply(error)


async def admin_unmute(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("Saya tidak dapat menemukan anggota itu.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    try:
        await message.chat.unban_member(user_id)
        await message.reply(f"<b>✅ {mention} sudah bisa chat lagi</b>")
    except Exception as error:
        await message.reply(error)


async def admin_unban(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("Saya tidak dapat menemukan anggota itu.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    try:
        await message.chat.unban_member(user_id)
        await message.reply(f"<b>✅ {mention} sudah bisa join lagi</b>")
    except Exception as error:
        await message.reply(error)


async def global_banned(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("🔄 Memproses...")
    if not user_id:
        return await Tm.edit("❌ Pengguna tidak ditemukan.")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = "<b>🚫 ɢʟᴏʙᴀʟ {}</b>\n\n<b>✅ Berhasil: {} ᴄʜᴀᴛ</b>\n<b>❌ Gagal: {} ᴄʜᴀᴛ</b>\n<b>👤 ᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a></b>"
    global_id = await get_global_id(client, "global")
    for dialog in global_id:
        if user.id == OWNER_ID:
            return await Tm.edit("❌ Anda tidak bisa gbanned dia karena dia pembuat saya.")
        try:
            await client.ban_chat_member(dialog, user.id)
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "ʙᴀɴɴᴇᴅ", done, failed, user.id, user.first_name, (user.last_name or "")
        )
    )
    return await Tm.delete()


async def global_unbanned(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("🔄 Memproses...")
    if not user_id:
        return await Tm.edit("❌ Pengguna tidak ditemukan.")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = "<b>🚫 ɢʟᴏʙᴀʟ {}</b>\n\n<b>✅ Berhasil: {} ᴄʜᴀᴛ</b>\n<b>❌ Gagal: {} ᴄʜᴀᴛ</b>\n<b>👤 ᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a></b>"
    global_id = await get_global_id(client, "global")
    for dialog in global_id:
        try:
            await client.unban_chat_member(dialog, user.id)
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "ᴜɴʙᴀɴɴᴇᴅ",
            done,
            failed,
            user.id,
            user.first_name,
            (user.last_name or ""),
        )
    )
    return await Tm.delete()
