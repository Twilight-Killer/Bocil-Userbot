from pykeyboard import InlineKeyboard
from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from PyroUbot import *


class Button:
    def alive(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="🗑️ ᴛᴜᴛᴜᴘ",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ]
        ]
        return button

    def button_add_expired(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} ʙᴜʟᴀɴ",
                    callback_data=f"success {user_id} {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton(
                "👤 ᴅᴀᴘᴀᴛᴋᴀɴ ᴘʀᴏꜰɪʟ 👤", callback_data=f"profil {user_id}"
            )
        )
        buttons.row(
            InlineKeyboardButton(
                "❌ ᴛᴏʟᴀᴋ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ❌", callback_data=f"failed {user_id}"
            )
        )
        return buttons

    def deak(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "⬅️ ᴋᴇᴍʙᴀʟɪ ",
                    callback_data=f"prev_ub {int(count)}",
                ),
                InlineKeyboardButton(
                    "sᴇᴛᴜJᴜɪ ✅", callback_data=f"deak_akun {int(count)}"
                ),
            ],
        ]
        return button

    def expired_button_bot():
        button = [
            [
                InlineKeyboardButton(
                    text=f"{bot.me.first_name}",
                    url=f"https://t.me/{bot.me.username}",
                )
            ]
        ]
        return button

    def start(message):
        if not message.from_user.id == OWNER_ID:
            button = [
                [InlineKeyboardButton("🔥 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 🔥", callback_data="bahan")],
                [
                    InlineKeyboardButton("✨ ʜᴇʟᴘ ᴍᴇɴᴜ", callback_data="help_back"),
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ 💬", callback_data="support"),
                ],
            ]
        else:
            button = [
                [InlineKeyboardButton("🔥 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 🔥", callback_data="bahan")],
                [
                    InlineKeyboardButton("🛠️ ɢɪᴛᴘᴜʟʟ", callback_data="gitpull"),
                    InlineKeyboardButton("ʀᴇsᴛᴀʀᴛ 🔁", callback_data="restart"),
                ],
                [
                    InlineKeyboardButton("🤖 ʟɪsᴛ ᴜsᴇʀʙᴏᴛ 🤖", callback_data="cek_ubot"),
                ],
            ]
        return button

    def plus_minus(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-𝟷 ʙᴜʟᴀɴ",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+𝟷 ʙᴜʟᴀɴ",
                    callback_data=f"tambah {query}",
                ),
            ],
            [InlineKeyboardButton("✅ ᴋᴏɴꜰɪʀᴍᴀsɪ ✅", callback_data="confirm")],
            [InlineKeyboardButton("❌ ʙᴀᴛᴀʟᴋᴀɴ ❌", callback_data=f"home {user_id}")],
        ]
        return button

    def userbot(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "📁 ʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ 📁",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "📲 ɢᴇᴛ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ 📲",
                    callback_data=f"get_phone {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "⏳ ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ ⏳",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔑 ɢᴇᴛ ᴄᴏᴅᴇ ᴏᴛᴘ 🔑",
                    callback_data=f"get_otp {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔐 ɢᴇᴛ ᴄᴏᴅᴇ 𝟸ғᴀ 🔐",
                    callback_data=f"get_faktor {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "☠ ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ ☠", callback_data=f"ub_deak {int(count)}"
                )
            ],
            [
                InlineKeyboardButton("⬅️", callback_data=f"prev_ub {int(count)}"),
                InlineKeyboardButton("➡️", callback_data=f"next_ub {int(count)}"),
            ],
        ]
        return button


class INLINE:
    def QUERY(func):
        async def wrapper(client, inline_query):
            users = ubot._get_my_id
            if inline_query.from_user.id not in users:
                await client.answer_inline_query(
                    inline_query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title=f"ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴏʀᴅᴇʀ @{bot.me.username}",
                                input_message_content=InputTextMessageContent(
                                    f"sɪʟᴀʜᴋᴀɴ ᴏʀᴅᴇʀ ᴅɪ @{bot.me.username} ᴅᴜʟᴜ ʙɪᴀʀ ʙɪsᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ɪɴʟɪɴᴇ ɪɴɪ"
                                ),
                            )
                        )
                    ],
                )
            else:
                await func(client, inline_query)

        return wrapper

    def DATA(func):
        async def wrapper(client, callback_query):
            users = ubot._get_my_id
            if callback_query.from_user.id not in users:
                await callback_query.answer(
                    f"ᴍᴀᴋᴀɴʏᴀ ᴏʀᴅᴇʀ ᴜsᴇʀʙᴏᴛ @{bot.me.username} ᴅᴜʟᴜ ʙɪᴀʀ ʙɪsᴀ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ɪɴɪ",
                    True,
                )
            else:
                try:
                    await func(client, callback_query)
                except MessageNotModified:
                    await callback_query.answer("❌ ERROR")

        return wrapper


async def create_button(m):
    buttons = InlineKeyboard(row_width=1)
    keyboard = []
    msg = []
    if "~>" not in m.text.split(None, 1)[1]:
        for X in m.text.split(None, 1)[1].split():
            X_parts = X.split(":", 1)
            keyboard.append(
                InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1])
            )
            msg.append(X_parts[0])
        buttons.add(*keyboard)
        if m.reply_to_message:
            text = m.reply_to_message.text
        else:
            text = " ".join(msg)
    else:
        for X in m.text.split("~>", 1)[1].split():
            X_parts = X.split(":", 1)
            keyboard.append(
                InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1])
            )
        buttons.add(*keyboard)
        text = m.text.split("~>", 1)[0].split(None, 1)[1]

    return buttons, text


# Inisialisasi aplikasi Pyrogram
app = Client("my_bot")

# Deklarasi variabel global untuk menyimpan tautan tombol yang sudah ada
buttons_text = "Pilih menu:\n[DANA](#dana)\n[OVO](#ovo)\n[QRIS](#qris)\n[BCA](#bca)\n[Kembali](#back)"
buttons_data = "dana\novo\nqris\nbca\nback"

# Fungsi untuk membuat tombol
async def notes_create_button(text):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = text.split("\n")
    for line in split_text[1:]:
        split_line = line.split("[", 1)
        button_text = split_line[0].replace("_", " ")
        if "](" in split_line[1]:
            button_url = split_line[1].split("](", 1)[1][:-1]
            keyboard.append(InlineKeyboardButton(button_text, url=button_url))
        else:
            button_data = split_line[1].replace("]", "")
            keyboard.append(InlineKeyboardButton(button_text, callback_data=button_data))
    buttons.add(*keyboard)

    text_button = split_text[0]
    return buttons, text_button

# Fungsi untuk memperbarui tombol-tombol
async def update_buttons():
    global buttons_text, buttons_data
    new_text = "Pilih menu:\n[DANA](#dana)\n[OVO](#ovo)\n[QRIS](#qris)\n[BCA](#bca)\n[Kembali](#back)\n[Tambah Menu](#add_menu)"
    new_data = "dana\novo\nqris\nbca\nback\nadd_menu"
    buttons_text = new_text
    buttons_data = new_data

# Example usage
async def example_usage():
    buttons, text_button = await notes_create_button(buttons_text)
    print(text_button)
    print(buttons)

# Fungsi untuk menangani tombol yang ditekan
@app.on_callback_query()
async def handle_callback_query(client, callback_query):
    data = callback_query.data
    if data == "dana":
        await callback_query.answer("Anda memilih DANA")
        # Tambahkan logika untuk menangani aksi terkait DANA di sini
    elif data == "ovo":
        await callback_query.answer("Anda memilih OVO")
        # Tambahkan logika untuk menangani aksi terkait OVO di sini
    elif data == "qris":
        await callback_query.answer("Anda memilih QRIS")
        # Tambahkan logika untuk menangani aksi terkait QRIS di sini
    elif data == "bca":
        await callback_query.answer("Anda memilih BCA")
        # Tambahkan logika untuk menangani aksi terkait BCA di sini
    elif data == "back":
        await callback_query.answer("Anda kembali ke menu sebelumnya")
        # Tambahkan logika untuk kembali ke menu sebelumnya di sini
    elif data == "add_menu":
        await update_buttons()
        await example_usage()
      
