import importlib
import random
from datetime import datetime, timedelta

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import *


async def login_cmd(client, message):
    info = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ...</b>", quote=True)
    if len(message.command) < 3:
        return await info.edit(
            f"<code>{message.text}</code> <b>ʜᴀʀɪ - sᴛʀɪɴɢ ᴘʏʀᴏɢʀᴀᴍ</b>"
        )
    try:
        ub = Ubot(
            name=f"ubot_{random.randrange(999999)}",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[2],
        )
        await ub.start()
        for mod in loadModule():
            importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
        now = datetime.now(timezone("Asia/Jakarta"))
        expire_date = now + timedelta(days=int(message.command[1]))
        await set_expired_date(ub.me.id, expire_date)
        await add_ubot(
            user_id=int(ub.me.id),
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[1],
        )
        buttons = [
            [
                InlineKeyboardButton(
                    "📁 ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ 📁",
                    callback_data=f"cek_masa_aktif {ub.me.id}",
                )
            ],
        ]
        await bot.send_message(
            LOGS_MAKER_UBOT,
            f"""
<b>❏ ᴜsᴇʀʙᴏᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ub.me.id}>{ub.me.first_name} {ub.me.last_name or ''}</a> 
<b> ╰ ɪᴅ:</b> <code>{ub.me.id}</code>
""",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
        )
        return await info.edit(
            f"<b>✅ ʙᴇʀʜᴀsɪʟ ʟᴏɢɪɴ ᴅɪ ᴀᴋᴜɴ: <a href='tg://user?id={ub.me.id}'>{ub.me.first_name} {ub.me.last_name or ''}</a></b>"
        )
    except Exception as error:
        return await info.edit(f"<code>{error}</code>")



@PY.CALLBACK("kontrol")
@INLINE.DATA
async def restart_confirm_callback(client, callback_query):
    user_id = callback_query.from_user.id
    
    for X in ubot._ubot:
        if user_id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        logging.debug("Removing and restarting userbot")
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        modules = loadModule()
                        for mod in modules:
                            importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))

                        back_button = InlineKeyboardButton("Kembali", callback_data="menu")
                        restart_button = InlineKeyboardButton("Restart", callback_data="kontrol")
                        keyboard = InlineKeyboardMarkup([[back_button, restart_button]])

                        datetime_str = datetime.now().strftime("%c")

                        result_text = (
                            f"<b>🇲🇨 restart berhasil dilakukan {UB.me.first_name} "
                            f"{UB.me.last_name or ''} | {UB.me.id}</b> ({datetime_str})"
                        )

                        await callback_query.edit_message_text(
                            result_text, reply_markup=keyboard
                        )

                    except Exception as error:
                        logging.error(f"Error occurred: {error}")
                        await callback_query.answer(f"Terjadi kesalahan saat merestart: {error}", show_alert=True)
                        return
