from PyroUbot import *

__MODULE__ = "blacklist"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʟᴀᴄᴋʟɪsᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addbll</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> memasukan group ke daftar hitam

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> menghapus grouo dari daftar hitam
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}rallbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> menghapus semua blacklist 
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}listbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> melihat semua daftar hitam
"""


@PY.UBOT("addbl")
async def _(client, message):
    await add_blacklist(client, message)


@PY.UBOT("unbl")
async def _(client, message):
    await del_blacklist(client, message)


@PY.UBOT("rallbl")
async def _(client, message):
    await rem_all_blacklist(client, message)


@PY.UBOT("listbl")
async def _(client, message):
    await get_blacklist(client, message)
