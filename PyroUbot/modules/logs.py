from pyrogram.enums import ChatType

from PyroUbot import *

__MODULE__ = "logs"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴀɴɢ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}logs</code> (on/off)
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴄʜᴀɴɴᴇʟ ʟᴏɢs
"""


@ubot.on_message(filters.group & filters.mentioned & filters.incoming, group=4)
@ubot.on_message(
    filters.private
    & filters.incoming
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.service, group=5
)
async def _(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")
    if logs and on_logs:
        if message.chat.type == ChatType.PRIVATE:
            type = "ᴘʀɪᴠᴀᴛᴇ"
            from_user = message.chat
            id_link = f"tg://openmessage?user_id={from_user.id}&message_id={message.id}"
        elif message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            type = "ɢʀᴏᴜᴘ"
            from_user = message.from_user
            id_link = message.link
        rpk = f"[{from_user.first_name} {from_user.last_name or ''}](tg://user?id={from_user.id})"
        link = f"[ᴋʟɪᴋ ᴅɪsɪɴɪ]({id_link})"
        await client.send_message(
            int(logs),
            f"""
<b>📩 ᴀᴅᴀ ᴘᴇsᴀɴ ᴍᴀsᴜᴋ</b>
    <b>•> ᴛɪᴘᴇ ᴘᴇsᴀɴ:</b> <code>{type}</code>
    <b>•> ʟɪɴᴋ ᴘᴇsᴀɴ:</b> {link}
    
<b>⤵️ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇsᴀɴ ᴛᴇʀᴜsᴀɴ ᴅᴀʀɪ: {rpk}</b>
""",
        )
        return await message.forward(int(logs))


@PY.UBOT("logs")
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply(
            "ʜᴀʀᴀᴘ ʙᴀᴄᴀ ᴍᴇɴᴜ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴄᴀʀᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴɴʏᴀ."
        )

    query = {"on": True, "off": False, "none": False}
    command = message.command[1].lower()

    if command not in query:
        return await message.reply("ᴏᴘsɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ʜᴀʀᴀᴘ ɢᴜɴᴀᴋᴀɴ 'on' ᴀᴛᴀᴜ 'off'.")

    value = query[command]

    vars = await get_vars(client.me.id, "ID_LOGS")

    if not vars:
        logs = await create_logs(client)
        await set_vars(client.me.id, "ID_LOGS", logs)

    if command == "none" and vars:
        try:
            await client.delete_channel(vars)
        except Exception:
            pass
        await set_vars(client.me.id, "ID_LOGS", value)

    await set_vars(client.me.id, "ON_LOGS", value)
    return await message.reply(
        f"<b>✅ <code>LOGS</code> ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴛɪɴɢ ᴋᴇ:</b> <code>{value}</code>"
    )


async def create_logs(client):
    logs = await client.create_channel(f"Logs Ubot: {bot.me.username}")
    await client.set_chat_photo(
        logs.id,
        photo="storage/Bocil_Logs.jpg",
    )
    return logs.id
