from PyroUbot import *

__MODULE__ = "gcast"
__HELP__ = """
<b>『 bantuan gcast 』</b>

  <b>• perintah:</b> <code>{0}ucast</code> [text/reply to text/media]
  <b>• penjelasan:</b> mengirim pesan ke chat 

  <b>• perintah:</b> <code>{0}gcast</code> [text/reply to text/media]
  <b>• penjelasan:</b> mengirim pesan ke group 

  <b>• perintah:</b> <code>{0}send</code> [userid/username to reply/text]
  <b>• penjelasan:</b> mengirim pesan ke group channel chat

    <b>• perintah:</b> auto_gcast (qury) - (value)
      <b>•> query & value:</b>
        <b>on/off:</b> untuk aktifkan dan nonaktifkan auto_gcast
        <b>text - kata-kata/reply_text:<b> menambahkan kata kata ke database
        <b>delay - angka:</b> merubah delay auto gcast
        <b>limit - on/off:</b> aktif/non-aktif untuk cek limit 15 menit sekali
  <b>• penjelasan:</b> mengerim pesan gcast otomatis 

  <b>• perintah:</b> <code>{0}gban</ᴄᴏᴅᴇ> [userid/username to reply/user]
  <b>• penjelasan:</b> banned pengguna 

  <b>• perintah:</b> <code>{0}ungban</code> [user_id/username to reply/user]
  <b>• penjelasan:</b> unban pengguna 
"""


@PY.UBOT("gcast")
async def _(client, message):
    await broadcast_group_cmd(client, message)


@PY.UBOT("ucast")
async def _(client, message):
    await broadcast_users_cmd(client, message)


@PY.BOT("send")
@PY.UBOT("send")
async def _(client, message):
    await send_msg_cmd(client, message)


@PY.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)


@PY.UBOT("gban")
async def _(client, message):
    await global_banned(client, message)


@PY.UBOT("ungban")
async def _(client, message):
    await global_unbanned(client, message)


AG = []
LT = []


@PY.UBOT("auto_gcast")
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>", quote=True)
    type, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT")

    if type == "on":
        if not auto_text_vars:
            return await msg.edit(
                "<b>ʜᴀʀᴀᴘ sᴇᴛᴛɪɴɢ ᴛᴇxᴛ ɢᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>"
            )

        if client.me.id not in AG:
            await msg.edit("<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>")

            AG.append(client.me.id)

            done = 0
            while client.me.id in AG:
                delay = await get_vars(client.me.id, "DELAY_GCAST") or 1
                blacklist = await get_chat(client.me.id)
                txt = random.choice(auto_text_vars)

                group = 0
                async for dialog in client.get_dialogs():
                    if (
                        dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
                        and dialog.chat.id not in blacklist
                    ):
                        try:
                            await asyncio.sleep(1)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except Exception as error:
                            print(f"Error sending message to {dialog.chat.id}: {error}")
                            continue

                if client.me.id not in AG:
                    return

                done += 1
                await msg.reply(
                    f"<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴘᴜᴛᴀʀᴀɴ {done} ʙᴇʀʜᴀsɪʟ ᴅᴀɴ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ: {group} ɢʀᴏᴜᴘ\n\nᴍᴇɴᴜɴɢɢᴜ {delay} ᴍᴇɴɪᴛ ʟᴀɢɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʟᴀɴɢ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ</b>",
                    quote=True,
                )
                await asyncio.sleep(int(60 * int(delay)))
        else:
            return await msg.delete()

    elif type == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit("<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇʟᴀʜ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ</b>")
        else:
            return await msg.delete()

    elif type == "text":
        if not value:
            return await msg.edit(
                "<b>ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇxᴛ ᴜɴᴛᴜᴋ ᴅɪ sɪᴍᴘᴀɴ sᴇʙᴀɢᴀɪ ᴛᴇxᴛ ᴀᴜᴛᴏ ɢᴄᴀsᴛ</b>"
            )
        await add_auto_text(client, value)
        return await msg.edit("<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ: ʙᴇʀʜᴀsɪʟ ᴅɪ sɪᴍᴘᴀɴ</b>")

    elif type == "delay":
        await set_vars(client.me.id, "DELAY_GCAST", value)
        return await msg.edit(
            f"<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴅᴇʟᴀʏ: ʙᴀʀʜᴀsɪʟ ᴋᴇ sᴇᴛᴛɪɴɢ {value} ᴍᴇɴɪᴛ</b>"
        )

    elif type == "remove":
        if not value:
            return await msg.edit(
                "<b>ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴀɴɢᴋᴀ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ʟɪsᴛ ᴛᴇxᴛ</b>"
            )
        if value == "all":
            await set_vars(client.me.id, "AUTO_TEXT", [])
            return await msg.edit("<b>sᴇᴍᴜᴀ ᴛᴇxᴛ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")
        try:
            value = int(value) - 1
            auto_text_vars.pop(value)
            await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
            return await msg.edit(
                f"<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ʀᴇᴍᴏᴠᴇ: ᴛᴇxᴛ ᴋᴇ {value+1} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs\n\nsɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ: <code>{message.text.split()[0]} list</code>, ᴋᴇᴍʙᴀʟɪ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴄᴇᴋ ᴀᴘᴀᴋᴀʜ sᴜᴅᴀʜ ᴛᴇʀʜᴀᴘᴜs</b>"
            )
        except Exception as error:
            return await msg.edit(str(error))

    elif type == "list":
        if not auto_text_vars:
            return await msg.edit("<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ ᴋᴏsᴏɴɢ</b>")
        txt = "<b>ᴅᴀғᴛᴀʀ ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ</b>\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"{num}: {x}\n\n"
        txt += f"<b>\nᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴛᴇxᴛ ᴋᴇᴛɪᴋ: <code>{message.text.split()[0]} remove ᴀɴɢᴋᴀ/ᴀʟʟ</code></b>"
        return await msg.edit(txt)

    elif type == "limit":
        if value == "off":
           if client.me.id in LT:
               LT.remove(client.me.id)
               return await msg.edit("<b>ᴀᴜᴛᴏ ᴄᴇᴋ ʟɪᴍɪᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ</b>")
           else:
               return await msg.edit("<b>ᴀᴜᴛᴏ ᴄᴇᴋ ʟɪᴍɪᴛ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ</b>")
   
    elif value == "on":
        if client.me.id not in LT:
            LT.append(client.me.id)
            await msg.edit("<b>ᴀᴜᴛᴏ ᴄᴇᴋ ʟɪᴍɪᴛ sᴛᴀʀᴛᴇᴅ</b>")
            while client.me.id in LT:
                for x in range(2):
                    await spam_bot(client, message)
                    await asyncio.sleep(5)
                await asyncio.sleep(1200)
        else:
            return await msg.edit("<b>ᴀᴜᴛᴏ ᴄᴇᴋ ʟɪᴍɪᴛ ᴛᴇʟᴀʜ ᴀᴋᴛɪғ</b>")
    else:
        return await msg.edit("<b>~ʜᴀʀᴀᴘ ᴍᴀsᴜᴋᴋᴀɴ ᴠᴀʟᴇᴜ ᴏɴ/ᴏғғ ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ</b>")

async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)


def extract_type_and_text(message):
    args = message.text.split(None, 2)
    if len(args) < 2:
        return None, None

    type = args[1]
    msg = (
        message.reply_to_message.text
        if message.reply_to_message
        else args[2]
        if len(args) > 2
        else None
    )
    return type, msg
