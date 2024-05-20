from gc import get_objects

from pykeyboard import InlineKeyboard
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from PyroUbot import *

FLOOD = {}
MSG_ID = {}
PM_TEXT = """
<b>🙋🏻‍♂️ ʜᴀʟᴏ {mention} ᴀᴅᴀ ʏᴀɴɢ ʙɪsᴀ sᴀʏᴀ ʙᴀɴᴛᴜ?

ᴘᴇʀᴋᴇɴᴀʟᴋᴀɴ sᴀʏᴀ ᴀᴅᴀʟᴀʜ ᴘᴍ-sᴇᴄᴜʀɪᴛʏ ᴅɪsɪɴɪ
sɪʟᴀʜᴋᴀɴ ᴛᴜɴɢɢᴜ ᴍᴀᴊɪᴋᴀɴ sᴀʏᴀ ᴍᴇᴍʙᴀʟᴀs ᴘᴇsᴀɴ ᴍᴜ ɪɴɪ ʏᴀ
ᴊᴀɴɢᴀɴ sᴘᴀᴍ ʏᴀ ᴀᴛᴀᴜ ᴀɴᴅᴀ ᴀᴋᴀɴ ᴅɪ ʙʟᴏᴋɪʀ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs

⛔ ᴘᴇʀɪɴɢᴀᴛᴀɴ: {warn} ʜᴀᴛɪ-ʜᴀᴛɪ</b>
"""

__MODULE__ = "pmpermit"
__HELP__ = """
<b>『 bantuan pmpermit  』</b>

  <b>• perintah:</b> <code>{0}pmpermit (on/off)</code>
  <b>• penjelasan:</b> mengaktifkan/non-aktifkan pmpermit

  <b>• perintah:</b> <code>{0}ok or {0}setuju</code>
  <b>• penjelasan:</b> setuju pm

  <b>• perintah:</b> <code>{0}setpmimage</code>
  <b>• penjelasan:</b> untuk set gambang pmpermit

  <b>• perintah:</b> <code>{0}no or {0}tolak</code>
  <b>• penjelasan:</b> nolak pm

  <b>• perintah:</b> <code>{0}setpm (query) (value)</code>
  <b>• penjelasan:</b> ngatur variabel text & limit

   <b>•> query:</b>
       •> <code>text</code>
       •> <code>limit</code>
"""


@ubot.on_message(
    filters.private & ~filters.bot & ~filters.service & filters.incoming, group=69
)

async def _(client, message):
    user = message.from_user
    pm_on = await get_vars(client.me.id, "PMPERMIT")
    if pm_on:
        if user.id == 777000:
            return
        if user.id != client.me.id:
            check = await get_pm_id(client.me.id)
            if user.id not in check:
                if user.id in FLOOD:
                    FLOOD[user.id] += 1
                else:
                    FLOOD[user.id] = 1
                if user.id in MSG_ID:
                    await delete_old_message(message, MSG_ID.get(user.id, 0))
                pm_limit = await get_vars(client.me.id, "PM_LIMIT") or "5"
                if FLOOD[user.id] > int(pm_limit):
                    del FLOOD[user.id]
                    await message.reply(
                        "sudah diingatkan jangan spam, mampuskan ke blokir."
                    )
                    return await client.block_user(user.id)
                pm_msg = await get_vars(client.me.id, "PM_TEXT") or PM_TEXT
                if "~>" in pm_msg:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"pm_pr {id(message)} {FLOOD[user.id]}"
                    )
                    msg = await client.send_inline_bot_result(
                        message.chat.id,
                        x.query_id,
                        x.results[0].id,
                        reply_to_message_id=message.id,
                    )
                    MSG_ID[user.id] = int(msg.updates[0].id)
                else:
                    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
                    peringatan = f"{FLOOD[user.id]} / {pm_limit}"
                    msg = await message.reply(
                        pm_msg.format(mention=rpk, warn=peringatan)
                    )
                    MSG_ID[user.id] = msg.id


@PY.UBOT("setpm")
async def _(client, message):
    if len(message.command) < 3:
        return await message.reply(
            "harap baca menu bantuan supaya paham."
        )
    query = {"limit": "PM_LIMIT", "text": "PM_TEXT"}
    if message.command[1].lower() not in query:
        return await message.reply("<b>❌ query yang lu masukan salah</b>")
    query_str, value_str = (
        message.text.split(None, 2)[1],
        message.text.split(None, 2)[2],
    )
    value = query[query_str]
    await set_vars(client.me.id, value, value_str)
    return await message.reply(
        f"<b>✅ <code>{value}</code> berhasil disetting ke: <code>{value_str}</code>"
    )


@PY.UBOT("setpmimage")
async def set_pm_image(client, message):
    if len(message.command) < 2:
        return await message.reply("Harap sertakan URL gambar untuk diset sebagai PM image.")
    image_url = message.command[1]
    await set_vars(client.me.id, "PM_IMAGE", image_url)
    return await message.reply(f"✅ Gambar PM berhasil disetting ke: {image_url}")


@PY.UBOT("pmpermit")
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply(
            "harap baca menu bantuan supaya paham."
        )

    toggle_options = {"off": False, "on": True}
    toggle_option = message.command[1].lower()

    if toggle_option not in toggle_options:
        return await message.reply("opsi salah. gunakan 'on' atau 'off'.")

    value = toggle_options[toggle_option]
    text = "diaktifkan" if value else "dinonaktifkan"

    await set_vars(client.me.id, "PMPERMIT", value)
    await message.reply(f"<b>✅ pmpermit berhasil{text}</b>")


@PY.INLINE("pm_pr")
async def _(client, inline_query):
    get_id = inline_query.query.split()
    m = [obj for obj in get_objects() if id(obj) == int(get_id[1])][0]
    pm_msg = await get_vars(m._client.me.id, "PM_TEXT") or PM_TEXT
    pm_limit = await get_vars(m._client.me.id, "PM_LIMIT") or 5
    rpk = f"[{m.from_user.first_name} {m.from_user.last_name or ''}](tg://user?id={m.from_user.id})"
    peringatan = f"{int(get_id[2])} / {pm_limit}"
    buttons, text = await pmpermit_button(pm_msg)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="Dapatkan tombol!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(
                        text.format(mention=rpk, warn=peringatan)
                    ),
                )
            )
        ],
    )


@PY.UBOT("ok|setuju")
@PY.PRIVATE
async def _(client, message):
    user = message.chat
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    vars = await get_pm_id(client.me.id)
    if user.id not in vars:
        await add_pm_id(client.me.id, user.id)
        return await message.reply(f"<b>✅ baikla, {rpk} telah diterima</b>")
    else:
        return await message.reply(f"<b>{rpk} sudah diterima</b>")


@PY.UBOT("no|tolak")
@PY.PRIVATE
async def _(client, message):
    user = message.chat
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    vars = await get_pm_id(client.me.id)
    if user.id not in vars:
        await message.reply(f"<b>🙏🏻 sory ⁣{rpk} anda diblokir kwkwkw</b>")
        return await client.block_user(user.id)
    else:
        await remove_pm_id(client.me.id, user.id)
        return await message.reply(
            f"<b>🙏🏻 maaf {rpk} anda telah ditolak </b>"
        )


async def pmpermit_button(m):
    buttons = InlineKeyboard(row_width=1)
    keyboard = []
    for X in m.split("~>", 1)[1].split():
        X_parts = X.split(":", 1)
        keyboard.append(
            InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1])
        )
    buttons.add(*keyboard)
    text = m.split("~>", 1)[0]

    return buttons, text


async def delete_old_message(message, msg_id):
    try:
        await message._client.delete_messages(message.chat.id, msg_id)
    except:
        pass
