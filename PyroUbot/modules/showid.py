from PyroUbot import *

__MODULE__ = "showid"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sʜᴏᴡɪᴅ 』</b>

  <b>• perintah:</b> <code>{0}id</code>
  <b>• penjelasan:</b> cek id group/channel/user

  <b>• penjelasan:</b> <code>{0}id</code> [reply user to media]
  <b>• perintah:</b> cek id media/user

  <b>• perintah:</b> <code>{0}id</code> [username/chanel/group]
  <b>• penjelasan:</b> cek id 
"""


@PY.UBOT("id")
async def _(client, message):
    await id_cmd(client, message)
