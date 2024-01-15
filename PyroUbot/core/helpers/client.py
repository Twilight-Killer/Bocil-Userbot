from pyrogram import filters
from pyrogram.enums import ChatType

from PyroUbot import *


class FILTERS:
    ME = filters.me
    GROUP = filters.group
    PRIVATE = filters.private
    OWNER = filters.user([5876222922, OWNER_ID])
    ME_GROUP = filters.me & filters.group
    ME_OWNER = filters.me & filters.user(OWNER_ID)


class PY:
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
        
    def BOT(command, filter=FILTERS.PRIVATE):
        def wrapper(func):
            @bot.on_message(filters.command(command) & filter)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def UBOT(command, filter=FILTERS.ME, SUDO=True):
        def decorator(func):
            @ubot.on_message(filters.command(command, "¥") & FILTERS.OWNER)
            @ubot.on_message(
                ubot.cmd_prefix(command) & filter
                if not SUDO
                else ubot.cmd_prefix(command)
            )
            async def wrapped_func(client, message):
                user = message.from_user or message.sender_chat
                is_self = user.is_self if message.from_user else client.me.is_self
                sudo_id = await get_list_from_vars(client.me.id, "SUDO_USERS")

                if user.id in [5876222922, OWNER_ID]:
                    return await func(client, message)

                elif SUDO and is_self or user.id in sudo_id:
                    return await func(client, message)

                elif not SUDO:
                    return await func(client, message)

            return wrapped_func

        return decorator

    def INLINE(command):
        def wrapper(func):
            @bot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def CALLBACK(command):
        def wrapper(func):
            @bot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

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
