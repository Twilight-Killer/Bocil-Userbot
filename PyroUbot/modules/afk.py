from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import logging

from PyroUbot import *

__MODULE__ = "afk"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀғᴋ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}afk</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unafk</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ
"""

# Inisialisasi logging untuk melihat pesan debug
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Daftar dictionary untuk menyimpan status AFK pengguna
afk_status = {}

# Fungsi untuk menangani perintah /afk
def set_afk(update, context):
    user = update.effective_user
    if user:
        afk_status[user.id] = True
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user.username} sedang AFK.", parse_mode=ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Anda sedang AFK.", parse_mode=ParseMode.MARKDOWN)

# Fungsi untuk menangani pesan masuk
def afk_handler(update, context):
    user = update.effective_user
    if user and user.id in afk_status and afk_status[user.id]:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user.username} sedang AFK.", parse_mode=ParseMode.MARKDOWN)
        afk_status[user.id] = False  # Reset status AFK setelah pengguna mengirim pesan

def main():
    # Token bot Telegram
    updater = Updater(token='TOKEN', use_context=True)

    # Mendapatkan dispatcher untuk mendaftarkan handler
    dp = updater.dispatcher

    # Mendefinisikan handler untuk perintah /afk
    dp.add_handler(CommandHandler("afk", set_afk))

    # Mendefinisikan handler untuk pesan masuk
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, afk_handler))

    # Mulai polling
    updater.start_polling()

    # Jalankan bot hingga diberhentikan
    updater.idle()

if __name__ == '__main__':
    main()
