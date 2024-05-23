from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import LOGS_MAKER_UBOT, OWNER_ID, bot, get_expired_date, ubot


class MSG:
    def DEAK(X):
        return (
            f"""
<b>❏ pemberitahuan</b>
<b>├ akun:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ id:</b> <code>{X.me.id}</code>
<b>╰ telah berhasil dihapus dari telegram</b>
""",
        )

    def EXPIRED_MSG_BOT(X):
        return f"""
<b>❏ pemberitahuan</b>
<b>├ akun:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ id:</b> <code>{X.me.id}</code>
<b>╰ masa aktif telah habis</b>
"""

    def START(message):
        if not message.from_user.id == OWNER_ID:
            msg = f"""
<b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

💬 @{bot.me.username} bot untuk membuat userbot dengan muda

👉🏻 klik tombol dibawah untuk membuat userbot</b>
"""
        else:
            msg = f"""
🧑‍💻 mode developer: <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>

✅ gunakan tombol dibawah dengan baik
"""
        return msg

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<b>💬 silahkan masukan pembayaran terlebih dahulu</b>

<b>🎟️ harga perbulan: {harga}.000</b>

<b>💳 metode pembayaran:</b>
 <b>├ dana/ovo</b>
 <b>├────• <code>085748237211</code></b>
 <b>├ qris</b>
 <b>└────• <a href=https://te.legra.ph/file/01f3251e08aedd5fa93c5.jpg>ᴋʟɪᴋ ᴅɪsɪɴɪ</a></b>

<b>🔖 total harga: ʀᴘ {total}.000</b>
<b>🗓️ total bulan: {bulan}</b> 

<b>✅ klik tombol dibawah ini untuk konfirmasi pembayaran anda</b>
"""

    def POLICY():
        return """
↪️ kebijakan kembalian

✅ sᴇᴛᴇʟᴀʜ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ, ᴊɪᴋᴀ ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴍᴇᴍᴘᴇʀᴏʟᴇʜ/
ᴍᴇɴᴇʀɪᴍᴀ ᴍᴀɴꜰᴀᴀᴛ ᴅᴀʀɪ ᴘᴇᴍʙᴇʟɪᴀɴ, 
ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʜᴀᴋ ᴘᴇɴɢɢᴀɴᴛɪᴀɴ ᴅᴀʟᴀᴍ ᴡᴀᴋᴛᴜ 2 ʜᴀʀɪ sᴇᴛᴇʟᴀʜ ᴘᴇᴍʙᴇʟɪᴀɴ. ɴᴀᴍᴜɴ, ᴊɪᴋᴀ 
ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ/ᴍᴇɴᴇʀɪᴍᴀ sᴀʟᴀʜ sᴀᴛᴜ ᴍᴀɴꜰᴀᴀᴛ ᴅᴀʀɪ 
ᴘᴇᴍʙᴇʟɪᴀɴ, ᴛᴇʀᴍᴀsᴜᴋ ᴀᴋsᴇs ᴋᴇ ꜰɪᴛᴜʀ ᴘᴇᴍʙᴜᴀᴛᴀɴ ᴜsᴇʀʙᴏᴛ, ᴍᴀᴋᴀ 
ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʟᴀɢɪ ʙᴇʀʜᴀᴋ ᴀᴛᴀs ᴘᴇɴɢᴇᴍʙᴀʟɪᴀɴ ᴅᴀɴᴀ.

🆘 ᴅᴜᴋᴜɴɢᴀɴ
ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴜᴋᴜɴɢᴀɴ, ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ:
• ᴍᴇɴɢʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ ᴅɪʙᴀᴡᴀʜ ɪɴɪ
• sᴜᴘᴘᴏʀᴛ @quntulharam ᴅɪ ᴛᴇʟᴇɢʀᴀᴍ

👉🏻 ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʟᴀɴᴊᴜᴛᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴʏᴀᴛᴀᴋᴀɴ ʙᴀʜᴡᴀ ᴀɴᴅᴀ ᴛᴇʟᴀʜ 
ᴍᴇᴍʙᴀᴄᴀ ᴅᴀɴ ᴍᴇɴᴇʀɪᴍᴀ ᴋᴇᴛᴇɴᴛᴜᴀɴ ɪɴɪ ᴅᴀɴ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ 
ᴘᴇᴍʙᴇʟɪᴀɴ. ᴊɪᴋᴀ ᴛɪᴅᴀᴋ, ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʙᴀᴛᴀʟᴋᴀɴ.
"""

    async def USERBOT(count):
        expired_date = await get_expired_date(ubot._ubot[int(count)].me.id)
        return f"""
<b>❏ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ├ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b> ╰ ᴇxᴘɪʀᴇᴅ</b> <code>{expired_date.strftime('%d-%m-%Y')}</code>
"""


async def sending_user(user_id):
    try:
        await bot.send_message(
            user_id,
            "💬 sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ᴀɴᴅᴀ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔥 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 🔥",
                            callback_data="bahan",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )
        await bot.send_message(
            LOGS_MAKER_UBOT,
            f"""
➡️ ʏᴀɴɢ ᴍᴇʀᴀsᴀ ᴍᴇᴍɪʟɪᴋɪ ɪᴅ: {user_id}

✅ sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ɴʏᴀ ᴅɪ: @{bot.me.username}
    """,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "📁 ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ 📁",
                            callback_data=f"cek_masa_aktif {user_id}",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        await bot.send_message(
            LOGS_MAKER_UBOT,
            f"""
➡️ ʏᴀɴɢ ᴍᴇʀᴀsᴀ ᴍᴇᴍɪʟɪᴋɪ ɪᴅ: {user_id}

✅ sɪʟᴀʜᴋᴀɴ ʙᴜᴀᴛ ᴜʟᴀɴɢ ᴜsᴇʀʙᴏᴛ ɴʏᴀ ᴅɪ: @{bot.me.username}
    """,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "📁 ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ 📁",
                            callback_data=f"cek_masa_aktif {user_id}",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )
