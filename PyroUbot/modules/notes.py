import re

from pyrogram.types import *
from pyrogram.errors import *

from PyroUbot import *

__MODULE__ = "notes"
__HELP__ = """
<b>『 bantuan notes 』</b>

  <b>• perintah:</b> <code>{0}save</code> [note_name - reply]
  <b>• penjelasan:</b> menyimpan catatan 

  <b>• perintah:</b> <code>{0}get</code> [note_name]
  <b>• penjelasan:</b> mengambil nama catatan 
 
  <b>• perintah:</b> <code>{0} rmnote</code> [note_name]
  <b>• penjelasan:</b> hapus catatan
 
  <b>• perintah:</b> <code>{0}notes</code>
  <b>• penjelasan:</b> melihat daftar catatan

  note: untuk menggunakan button - gunakan fotmat:
  <code>text | nama tombol - url/callback |</code>
 """



def detect_url_links(text):
    link_pattern = r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:[/?]\S+)?|tg://\S+"
    link_found = re.findall(link_pattern, text)
    return link_found


def button_and_text(text):
    button_matches = re.findall(r"\| ([^|]+) - ([^|]+) \|", text)
    text_matches = (
        re.split(r"\| [^|]+ - [^|]+ \|", text)[0].strip()
        if "|" in text
        else text.strip()
    )
    return button_matches, text_matches
  

def create_inline_keyboard(text, type=None, is_back=False):
    """
    cara menggunakan:
                    contoh text:
                               klik tombol di bawah | situs google - https://goggle.com |
                    contoh text dengan metode ;same:
                                                   klik tombol di bawah | situs google - https://goggle.com | | situs youtube - https://youtube.com;same |

    """
    keyboard = []
    button_matches, text_matches = button_and_text(text)

    for button_text, button_data in button_matches:
        cb_data = (
            button_data.split(";same")[0]
            if detect_url_links(button_data.split(";same")[0])
            else (
                f"_gtnote {int(type.split('_')[0])}_{type.split('_')[1]} {button_data.split(';same')[0]}"
                if type
                else button_data.split(";same")[0]
            )
        )

        add_button = (
            InlineKeyboardButton(button_text, url=cb_data)
            if detect_url_links(cb_data)
            else InlineKeyboardButton(button_text, callback_data=cb_data)
        )
        if ";same" in button_data and keyboard:
            keyboard[-1].append(add_button)
        else:
            keyboard.append([add_button])

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    if type and is_back:
        markup.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    "kembali",
                    f"_gtnote {int(type.split('_')[0])}_{type.split('_')[1]}",
                )
            ]
        )

    return markup, text_matches
  

@PY.UBOT("save|ssave")
async def _(client, message):
    args = get_arg(message)
    reply = message.reply_to_message
    query = "notes_cb" if message.command[0] == "ssave" else "notes"

    if not args or not reply:
        return await message.reply(
            f"<code>{message.text.split()[0]}</code> <b>[name] [text/reply]</b>"
        )

    vars = await get_vars(client.me.id, args, query)

    if vars:
        return await message.reply(f"<b>catatan {args} suda ada</n>")

    value = None
    type_mapping = {
        "text": reply.text,
        "photo": reply.photo,
        "voice": reply.voice,
        "audio": reply.audio,
        "video": reply.video,
        "animation": reply.animation,
        "sticker": reply.sticker,
    }

    for media_type, media in type_mapping.items():
        if media:
            send = await reply.copy(client.me.id)
            value = {
                "type": media_type,
                "message_id": send.id,
            }
            break

    if value:
        await set_vars(client.me.id, args, value, query)
        return await message.reply(
            f"<b>ᴄᴀᴛᴀᴛᴀɴ <code>{args}</code> berhasil disimpan di database ✅</b>"
        )
    else:
        return await message.reply(
            f"<code>{message.text.split()[0]}</code> <b>[name] [text/reply]</b>"
        )


@PY.UBOT("rmnote|srmnote")
async def _(client, message):
    args = get_arg(message)

    if not args:
        return await message.reply(
            f"<code>{message.text.split()[0]}</code> <b>[name]</b>"
        )

    query = "notes_cb" if message.command[0] == "srmnote" else "notes"
    vars = await get_vars(client.me.id, args, query)

    if not vars:
        return await message.reply(f"<b>catatan {args} tidak ditemukan</b>")

    await remove_vars(client.me.id, args, query)
    await client.delete_messages(client.me.id, int(vars["message_id"]))
    return await message.reply(f"<b>catatan {args} berhasil dihapus❎</b>")


@PY.UBOT("get")
async def _(client, message):
    msg = message.reply_to_message or message
    args = get_arg(message)

    if not args:
        return await message.reply(
            f"<code>{message.text.split()[0]}</code> <b>[name]</b>"
        )

    data = await get_vars(client.me.id, args, "notes")

    if not data:
        return await message.reply(
            f"<b>catatan {args} tidak di temukan</b>"
        )

    m = await client.get_messages(client.me.id, int(data["message_id"]))

    if data["type"] == "text":
        if matches := re.findall(r"\| ([^|]+) - ([^|]+) \|", m.text):
            try:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"get_notes {client.me.id} {args}"
                )
                return await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=msg.id,
                )
            except Exception as error:
                await message.reply(error)
        else:
            return await m.copy(message.chat.id, reply_to_message_id=msg.id)
    else:
        return await m.copy(message.chat.id, reply_to_message_id=msg.id)


@PY.UBOT("notes|snotes")
async def _(client, message):
    query = "notes_cb" if message.command[0] == "snotes" else "notes"
    vars = await all_vars(client.me.id, query)
    if vars:
        msg = "<b>❏ ᴅᴀғᴛᴀʀ ᴄᴀᴛᴀᴛᴀɴ</b>\n\n"
        for x, data in vars.items():
            msg += f"<b> •> <code>{x}</code> | {data['type']}</b>\n"
        msg += f"<b>\n❏ total catatan: {len(vars)}</b>"
    else:
        msg = "<b>tidak ada catatan</b>"

    return await message.reply(msg, quote=True)


@PY.INLINE("^get_notes")
@INLINE.QUERY
async def _(client, inline_query):
    query = inline_query.query.split()
    data = await get_vars(int(query[1]), query[2], "notes")
    item = [x for x in ubot._ubot if int(query[1]) == x.me.id]
    for me in item:
        m = await me.get_messages(int(me.me.id), int(data["message_id"]))
        buttons, text = create_inline_keyboard(m.text, f"{int(query[1])}_{query[2]}")
        return await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                (
                    InlineQueryResultArticle(
                        title="get notes!",
                        reply_markup=buttons,
                        input_message_content=InputTextMessageContent(text),
                    )
                )
            ],
        )


@PY.CALLBACK("_gtnote")
async def _(client, callback_query):
    _, user_id, *query = callback_query.data.split()
    data_key = "notes_cb" if bool(query) else "notes"
    query_eplit = query[0] if bool(query) else user_id.split("_")[1]
    data = await get_vars(int(user_id.split("_")[0]), query_eplit, data_key)
    item = [x for x in ubot._ubot if int(user_id.split("_")[0]) == x.me.id]
    for me in item:
        m = await me.get_messages(int(me.me.id), int(data["message_id"]))
        buttons, text = create_inline_keyboard(
            m.text, f"{int(user_id.split('_')[0])}_{user_id.split('_')[1]}", bool(query)
        )
        try:
            if "answer" in text:
                return await callback_query.answer(text.split("answer")[1], True)
            else:
                return await callback_query.edit_message_text(text, reply_markup=buttons)
        except MessageNotModified:
            return await callback_query.answer("❌ ERROR")
