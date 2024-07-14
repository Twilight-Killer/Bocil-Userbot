from pyrogram import filters
from pyrogram.enums import ChatType

from PyroUbot import *


async def if_sudo(_, client, message) -> bool:
    try:
        sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")
    except Exception:
        return False

    return message.from_user is not None and (
        message.from_user.id in sudo_users or message.from_user.is_self
    )

    

class FILTERS:
    ME = filters.me
    GROUP = filters.group
    PRIVATE = filters.private
    OWNER = filters.user([OWNER_ID])
    ME_GROUP = filters.me & filters.group
    ME_OWNER = filters.me & filters.user(OWNER_ID)
    SUDO = filters.create(if_sudo)


class PY:
    @staticmethod
    def AFK():
        def wrapper(func):
            afk_check = (
                (filters.mentioned | filters.private)
                & ~filters.bot
                & ~filters.me
                & filters.incoming
            )

            @ubot.on_message(afk_check, group=10)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def BOT(command, filter=False):
        def wrapper(func):
            message_filters = filters.command(command) & filter if filter else filters.command(command)
            @bot.on_message(message_filters)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def UBOT(command, filter=FILTERS.SUDO):
        def decorator(func):
            @ubot.on_message(ubot.cmd_prefix(command) & filter)
            async def wrapped_func(client, message):
                return await func(client, message)

            return wrapped_func

        return decorator

   
    @staticmethod
    def INLINE(command):
        def wrapper(func):
            @bot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def CALLBACK(command):
        def wrapper(func):
            @bot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def PRIVATE(func):
        async def function(client, message):
            user = message.from_user
            rpk = f"<a href='tg://user?id={user.id}'>{user.first_name} {user.last_name or ''}</a>"
            if not message.chat.type == ChatType.PRIVATE:
                return await message.reply(
                    f"<b>❌ ᴍᴀᴀғ {rpk}, ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ʜᴀɴʏᴀ ʙᴇʀғᴜɴɢsɪ ᴅɪ ᴘʀɪᴠᴀᴛᴇ.</b>",
                    quote=True,
                )
            return await func(client, message)

        return function
