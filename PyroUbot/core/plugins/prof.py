from pyrogram import Client, filters
from pyrogram.types import Message
from asyncio import gather
from os import remove

from PyroUbot import *


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


async def info_cmd(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("Processing...")
    if not user_id:
        return await Tm.edit("Berikan user ID/username/reply untuk mendapatkan info pengguna tersebut.")
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        user_details = (await client.get_chat(user.id)).bio
        bio = user_details if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""
User Information:

🆔 User ID: {user.id}
👤 First Name: {first_name}
🗣️ Last Name: {last_name}
🌐 Username: {username}
🏛️ DC ID: {dc_id}
🤖 Is Bot: {user.is_bot}
🚷 Is Scam: {user.is_scam}
🚫 Restricted: {user.is_restricted}
✅ Verified: {user.is_verified}
⭐ Premium: {user.is_premium}
📝 Bio: {bio}

👀 Same Groups Seen: {len(common)}
👁️ Last Seen: {status}
🔗 User Permanent Link: <a href="tg://user?id={user.id}">{fullname}</a>
"""
        photo_id = user.photo.big_file_id if user.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Tm.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=message.id,
                ),
            )
            remove(photo)
        else:
            await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"Info: {e}")



async def cinfo_cmd(client, message):
    Tm = await message.reply("Processing...")
    try:
        if len(message.text.split()) > 1:
            chat_u = message.text.split()[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await Tm.edit(
                    "Gunakan perintah ini di dalam grup atau gunakan cinfo [group username atau ID]"
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = chat.description if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""
Chat Information:

🆔 Chat ID: {chat.id}
👥 Title: {chat.title}
👥 Username: {username}
📩 Type: {type}
🏛️ DC ID: {dc_id}
🗣️ Is Scam: {chat.is_scam}
🎭 Is Fake: {chat.is_fake}
✅ Verified: {chat.is_verified}
🚫 Restricted: {chat.is_restricted}
🔰 Protected: {chat.has_protected_content}

🚻 Total Members: {chat.members_count}
📝 Description: {description}
"""
        photo_id = chat.photo.big_file_id if chat.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Tm.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=message.id,
                ),
            )
            remove(photo)
        else:
            await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"Info: {e}")

