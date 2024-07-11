from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *


@PY.BOT("control")
async def start_command(client, message):
    start_message = "𝐬𝐢𝐥𝐚𝐤𝐚𝐧 𝐩𝐢𝐥𝐢𝐡 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐲𝐚𝐧𝐠 𝐢𝐧𝐠𝐢𝐧 𝐚𝐧𝐝𝐚 𝐠𝐮𝐧𝐚𝐤𝐚𝐧 ⏬"
    menu_button = InlineKeyboardButton("𝐦𝐞𝐧𝐮", callback_data="menu")
    url_button = InlineKeyboardButton("ǫʀɪs", url="https://graph.org/file/c35c2078ee9b4155608d4.jpg")
    keyboard = InlineKeyboardMarkup([[menu_button, url_button]])
    await message.reply_text(start_message, reply_markup=keyboard)


@PY.CALLBACK("dana")
async def dana_callback(client, callback_query):
    dana_text = """💰dana
ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴍᴇʟᴀʟᴜɪ ᴅᴀɴᴀ ɢᴜɴᴀᴋᴀɴ ɴᴏᴍᴏʀ ᴛᴜᴊᴜᴀɴ ʙᴇʀɪᴋᴜᴛ:
085748237211 ᴀ/ɴ ʜᴀᴍxxxx Mᴜʜᴀᴍxx ʀɪᴅxx
sᴇᴛᴇʟᴀʜ ᴀɴᴅᴀ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ,
ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʙᴀᴄᴋ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴋᴇᴍʙᴀʟɪ"""
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="menu")]])
    await callback_query.edit_message_text(dana_text, reply_markup=keyboard)
    

@PY.CALLBACK("ovo")
async def dana_callback(client, callback_query):
    ovo_text = """💰ᴏᴠᴏ
ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴍᴇʟᴀʟᴜɪ ᴏᴠᴏ ɢᴜɴᴀᴋᴀɴ ɴᴏᴍᴏʀ ᴛᴜᴊᴜᴀɴ ʙᴇʀɪᴋᴜᴛ:
085748237211 ᴀ/ɴ ʜᴀᴍxxxx Mᴜʜᴀᴍxx ʀɪᴅxx
sᴇᴛᴇʟᴀʜ ᴀɴᴅᴀ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ,
ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʙᴀᴄᴋ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴋᴇᴍʙᴀʟɪ"""
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="menu")]])
    await callback_query.edit_message_text(ovo_text, reply_markup=keyboard)


@PY.CALLBACK("gopay")
async def dana_callback(client, callback_query):
    gopay_text = """💰gopay
ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴍᴇʟᴀʟᴜɪ ɢᴏᴘᴀʏ ɢᴜɴᴀᴋᴀɴ ɴᴏᴍᴏʀ ᴛᴜᴊᴜᴀɴ ʙᴇʀɪᴋᴜᴛ:
085748237211 ᴀ/ɴ ʜᴀᴍxxxx Mᴜʜᴀᴍxx ʀɪᴅxx
sᴇᴛᴇʟᴀʜ ᴀɴᴅᴀ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ,
ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʙᴀᴄᴋ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴋᴇᴍʙᴀʟɪ"""
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="menu")]])
    await callback_query.edit_message_text(gopay_text, reply_markup=keyboard)


@PY.CALLBACK("menu")
async def menu_callback(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("sᴛᴀᴛs 🇲🇨", callback_data="stats")],
        [InlineKeyboardButton("ᴅᴀɴᴀ 💳", callback_data="dana"),
         InlineKeyboardButton("ʀᴇsᴛᴀʀᴛ ✅", callback_data="kontrol")],
        [InlineKeyboardButton("ᴏᴠᴏ 📩", callback_data="ovo"),
         InlineKeyboardButton("ɢᴏᴘᴀʏ", callback_data="gopay")],
        [InlineKeyboardButton("🔁", callback_data="back")]
    ])
    await callback_query.edit_message_text("HALO MEK PENCET MENU DI BAWAH YA ADA PILAHAN YANG LU MAU :", reply_markup=keyboard)

@PY.CALLBACK("back")
async def back_callback(client, callback_query):
    start_message = "𝐬𝐢𝐥𝐚𝐤𝐚𝐧 𝐩𝐢𝐥𝐢𝐡 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐲𝐚𝐧𝐠 𝐢𝐧𝐠𝐢𝐧 𝐚𝐧𝐝𝐚 𝐠𝐮𝐧𝐚𝐤𝐚𝐧 ⏬:"
    menu_button = InlineKeyboardButton("𝐦𝐞𝐧𝐮", callback_data="menu")
    url_button = InlineKeyboardButton("ǫʀɪs", url="https://graph.org/file/c35c2078ee9b4155608d4.jpg")
    keyboard = InlineKeyboardMarkup([[menu_button, url_button]])
    await callback_query.edit_message_text(start_message, reply_markup=keyboard)
