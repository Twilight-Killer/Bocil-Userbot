from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *

@PY.BOT("control")
async def start_command(client, message):
    start_message = "𝐬𝐢𝐥𝐚𝐤𝐚𝐧 𝐩𝐢𝐥𝐢𝐡 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 𝐲𝐚𝐧𝐠 𝐢𝐧𝐠𝐢𝐧 𝐚𝐧𝐝𝐚 𝐠𝐮𝐧𝐚𝐤𝐚𝐧 ⏬"
    menu_button = InlineKeyboardButton("𝐦𝐞𝐧𝐮", callback_data="menu")
    url_button = InlineKeyboardButton("ǫʀɪs", url="https://graph.org/file/c35c2078ee9b4155608d4.jpg")
    keyboard = InlineKeyboardMarkup([[menu_button, url_button]])
    await message.reply_text(start_message, reply_markup=keyboard)

@PY.CALLBACK("command1")
async def command1_callback(client, callback_query):
    await callback_query.answer("Hontol.....")
    back_button = InlineKeyboardButton("Back", callback_data="menu")
    keyboard = InlineKeyboardMarkup([[back_button]])
    await callback_query.edit_message_text("HA•• MUH••• RI•••:085748237211", reply_markup=keyboard)

@PY.CALLBACK("command2")
async def command2_callback(client, callback_query):
    await callback_query.answer("Hontol.....")
    back_button = InlineKeyboardButton("Back", callback_data="menu")
    keyboard = InlineKeyboardMarkup([[back_button]])
    await callback_query.edit_message_text("KONTOL BELUM ADA ", reply_markup=keyboard)

@PY.CALLBACK("command3")
async def command3_callback(client, callback_query):
    await callback_query.answer("Hontol.....")
    back_button = InlineKeyboardButton("Back", callback_data="menu")
    keyboard = InlineKeyboardMarkup([[back_button]])
    await callback_query.edit_message_text("MEMEK BELUM ADA JUGA ", reply_markup=keyboard)

@PY.CALLBACK("command4")
async def command4_callback(client, callback_query):
    await callback_query.answer("Hontol.....")
    back_button = InlineKeyboardButton("Back", callback_data="menu")
    keyboard = InlineKeyboardMarkup([[back_button]])
    await callback_query.edit_message_text("YAH KEPO YA", reply_markup=keyboard)

@PY.CALLBACK("menu")
async def menu_callback(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("sᴛᴀᴛs 🇲🇨", callback_data="stats")],
        [InlineKeyboardButton("ᴅᴀɴᴀ 💳", callback_data="command1"),
         InlineKeyboardButton("ʀᴇsᴛᴀʀᴛ ✅", callback_data="restart")],
        [InlineKeyboardButton("ʙᴇʟɪ ʙᴏᴛ 📩", callback_data="command3"),
         InlineKeyboardButton("ᴍᴇᴍᴇᴋ", callback_data="command4")],
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
