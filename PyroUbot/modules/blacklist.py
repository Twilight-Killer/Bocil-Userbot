from PyroUbot import *

__MODULE__ = "blacklist"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ blacklist 』</b>

  <b>• perinta:</b> <code>{0}addbll</code>
  <b>• penjelasan:</b> memasukan group ke daftar hitam

  <b>• perintah:</b> <code>{0}unbl</code>
  <b>• penjelasan:</b> menghapus grouo dari daftar hitam
  
  <b>• perintah:</b> <code>{0}rallbl</code>
  <b>• penjelasan:</b> menghapus semua blacklist 
  
  <b>• perintah:</b> <code>{0}listbl</code>
  <b>• penjelasan:</b> melihat semua daftar hitam
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
