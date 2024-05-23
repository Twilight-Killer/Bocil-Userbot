import asyncio
from datetime import datetime

from pyrogram.types import InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import bot, ubot
from PyroUbot.config import LOGS_MAKER_UBOT, OWNER_ID
from PyroUbot.core.database import *
from PyroUbot.core.helpers import MSG, Button


async def handle_expired_userbot(X):
    try:
        vars = await get_vars(X.me.id, "EXPIRED_DATE")
        
        if vars is None:
            raise ValueError("Expiration date not found for userbot")

        current_time = datetime.now(timezone("Asia/Jakarta"))
        exp = vars.astimezone(timezone("Asia/Jakarta"))
        
        if current_time.date() == exp.date():
            await X.unblock_user(bot.me.username)
            for chat in await get_chat(X.me.id):
                await remove_chat(X.me.id, chat)
            await rm_all(X.me.id)
            await remove_all_vars(X.me.id)
            await remove_ubot(X.me.id)
            await rem_uptime(X.me.id)
            await rem_expired_date(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            del ubot._get_my_peer[X.me.id]
            await bot.send_message(
                LOGS_MAKER_UBOT,
                MSG.EXPIRED_MSG_BOT(X),
                reply_markup=Button.expired_button_bot(),
            )
            await X.log_out()
    except Exception as e:
        await bot.send_message(OWNER_ID, f"Error: - {X.me.id}\n{str(e)}")


async def expiredUserbots():
    while True:
        get_ubot = [handle_expired_userbot(X) for X in ubot._ubot]
        await asyncio.gather(*get_ubot)
        await asyncio.sleep(10)
