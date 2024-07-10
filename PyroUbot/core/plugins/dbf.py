from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import *

# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℙℝ𝔼𝕄𝕀𝕌𝕄 #
# ========================== #


async def prem_user(client, message):
    Tm = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    if message.from_user.id not in await get_seles():
        return await Tm.edit(
            "untuk menggunakan perintah ini harus jadi seles dulu"
        )
    user_id, get_bulan = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<b>{message.text} user_id/username - bulan</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(str(error))
    if not get_bulan:
        get_bulan = 1
    premium = await get_prem()
    if user.id in premium:
        return await Tm.edit("sudah bisa membuat userbot")
    added = await add_prem(user.id)
    if added:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user.id, expired)
        info_msg = (
            "💬 information\n"
            f" name: {user.first_name} {user.last_name or ''}\n"
            f" id: {user.id}\n"
            " keterangan: premium\n"
            f" expired: {get_bulan} ʙᴜʟᴀɴ\n"
            f" buat userbot di @{bot.me.username}"
        )
        await Tm.edit(info_msg)
        await bot.send_message(
            OWNER_ID,
            f"• {message.from_user.id} ─> {user_id} •",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "👤 profil",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "profil 👤", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    else:
        await Tm.delete()
        await message.reply_text("terjadi kesalanhan tidak diketahui ")


async def unprem_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>prosesssss . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>balas ke pengguna atau gunakan user_id/username</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delpremium = await get_prem()
    if user.id not in delpremium:
        return await Tm.edit("<b>tidak ditemukan</b>")
    removed = await remove_prem(user.id)
    if removed:
        await Tm.edit(f"<b> ✅ {user.mention} berhasil dihapus ❌</b>")
    else:
        await Tm.delete()
        await message.reply_text("terjadi kesalanhan tidak diketahui")


async def get_prem_user(client, message):
    text = ""
    count = 0
    for user_id in await get_prem():
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{userlist}\n"
    if not text:
        await message.reply_text("tidak ada pengguna yang di temukan")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔹𝕃𝔸ℂ𝕂𝕃𝕀𝕊𝕋 #
# ========================== #


async def add_blacklist(client, message):
    Tm = await message.reply("<b>sabar dulu . . .</b>")
    if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
        chat_id = message.chat.id
        blacklist = await get_chat(client.me.id)
        if chat_id in blacklist:
            return await Tm.edit("group ini sudah ada di blacklist ")
        add_blacklist = await add_chat(client.me.id, chat_id)
        if add_blacklist:
            return await Tm.edit(
                f"group:{message.chat.title}\n keterangan: diblacklist"
            )
        else:
            return await Tm.edit("terjadi kesalanhan tidak diketahui")
    else:
        return await Tm.edit("perintah ini berguna di group")

async def del_blacklist(client, message):
    Tm = await message.reply("<b>sabar dulu . . .</b>")
    if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
        try:
            if not get_arg(message):
                chat_id = message.chat.id
            else:
                chat_id = int(message.command[1])
            blacklist = await get_chat(client.me.id)
            if chat_id not in blacklist:
                return await Tm.edit(
                    f"{message.chat.title} tidak ada daftar hitam"
                )
            del_blacklist = await remove_chat(client.me.id, chat_id)
            if del_blacklist:
                return await Tm.edit(f"{chat_id}\n\n keterangan: berhasil di hapus dari daftar hitam ❌")
            else:
                return await Tm.edit("terjadi kesalanhan tidak diketahui")
        except Exception as error:
            return await Tm.edit(error)
    else:
        return await Tm.edit("perintah ini berguna di group")


async def get_blacklist(client, message):
    Tm = await message.reply("<b>sabar dulu . . .</b>")
    msg = f"<b>• ᴛᴏᴛᴀʟ ʙʟᴀᴄᴋʟɪsᴛ {len(await get_chat(client.me.id))}</b>\n\n"
    for X in await get_chat(client.me.id):
        try:
            get = await client.get_chat(X)
            msg += f"<b>• {get.title} | <code>{get.id}</code></b>\n"
        except:
            msg += f"<b>• <code>{X}</code></b>\n"
    await Tm.delete()
    await message.reply(msg)


async def rem_all_blacklist(client, message):
    msg = await message.reply("<b>sabar dulu....</b>", quote=True)
    get_bls = await get_chat(client.me.id)
    if len(get_bls) == 0:
        return await msg.edit("<b>daftar hitam kosong</b>")
    for X in get_bls:
        await remove_chat(client.me.id, X)
    await msg.edit("<b>semua daftar hitam berhasil di hapus✅</b>")


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℝ𝔼𝕊𝔼𝕃𝕃𝔼ℝ #
# ========================== #


async def seles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>prosessss......</b>")
    if not user_id:
        return await Tm.edit(
            "<b>balas ke pengguna atau gunakan user_id/username</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    reseller = await get_seles()
    if user.id in reseller:
        return await Tm.edit("sudah menjadi reseller.")
    added = await add_seles(user.id)
    if added:
        await add_prem(user.id)
        await Tm.edit(f"<b>✅ {user.mention} telah menjadi reseller</b>")
    else:
        await Tm.delete()
        await message.reply_text("terjadi kesalanhan tidak diketahui")


async def unseles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>prosessss.....</b>")
    if not user_id:
        return await Tm.edit(
            "<b>balas ke pengguna atau gunakan user_id/username</n>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delreseller = await get_seles()
    if user.id not in delreseller:
        return await Tm.edit("tidak ditemukan")
    removed = await remove_seles(user.id)
    if removed:
        await remove_prem(user.id)
        await Tm.edit(f"{user.mention} berhasil dihapus✅")
    else:
        await Tm.delete()
        await message.reply_text("terjadi kesalanhan tidak diketahui")


async def get_seles_user(cliebt, message):
    text = ""
    count = 0
    for user_id in await get_seles():
        try:
            user = await bot.get_users(user_id)
            count += 1
            user = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{user}\n"
    if not text:
        await message.reply_text("tidak ada pengguna yamg di temukan")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔼𝕏ℙ𝕀ℝ𝔼𝔻 #
# ========================== #


async def expired_add(client, message):
    Tm = await message.reply("<b>prosesss......</b>")
    user_id, get_day = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<b>{message.text} user_id/username - hari</b>")
    elif user_id not in ubot._get_my_id:
        return await Tm.edit(f"<b>{user_id} tidak ada dalam system</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(
            "💬 information\n"
            f" name: {user.first_name} {user.last_name or ''}\n"
            f" id: {user.id}\n"
            f" expired_selama: {get_day}hari\n"
             " keterangan: tambah expired\n"
    )


async def expired_cek(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply("pengguna tidak ditemukan")
    user = await client.get_users(user_id)
    expired_date = await get_expired_date(user_id) if user_id in ubot._get_my_id else None
    prefix = ", ".join(ubot._prefix.get(user_id, [".", ",", ":", ";", "!"]))
    if expired_date is None:
        await message.reply(
            "💬 information\n"
            f" name: {user.first_name} {user.last_name or ''}\n"
            f" id: {user.id}\n"
            f" expired: {expired_date}\n"
             " keterangan: belum diaktifkan\n"
            f" prefix: {prefix}\n"
        )
    else:
        remaining_days = (expired_date - datetime.now()).days
        prefix = ", ".join(ubot._prefix.get(user_id, [".", ",", ":", ";", "!"]))
        await message.reply(
            "💬 information\n"
            f" name: {user.first_name} {user.last_name or ''}\n"
            f" id: {user.id}\n"
            f" expired: {remaining_days} hari\n"
            f" prefix: {prefix}\n"
        )


async def un_expired(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("</b>prosessss.....</b>")
    if not user_id:
        return await Tm.edit("<b>user tidak ditemukan</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    await rem_expired_date(user.id)
    return await Tm.edit(f"<b>✅ {user.id} expired telah habis</b>")
