from PyroUbot import *

__MODULE__ = "copy"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏᴘʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}copy</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴘᴇsᴀɴ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇʟᴀʟᴜɪ ʟɪɴᴋ ᴍᴇʀᴇᴋᴀ


  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}wow</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ ᴛɪᴍᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴍᴇᴅɪᴀ ᴛɪᴍᴇʀ ᴅᴀɴ ᴍᴇɴʏɪᴍᴘᴀɴ ᴋᴇ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ
"""


@PY.BOT("copy")
async def _(client, message):
    await copy_bot_msg(client, message)


@PY.UBOT("copy")
async def _(client, message):
    await copy_ubot_msg(client, message)


@PY.INLINE("^get_msg")
@INLINE.QUERY
async def _(client, inline_query):
    await copy_inline_msg(client, inline_query)


@PY.CALLBACK("^copymsg")
@INLINE.DATA
async def _(client, callback_query):
    await copy_callback_msg(client, callback_query)


@PY.UBOT("wow")
async def _(client, message):
    await colong_cmn(client, message)
