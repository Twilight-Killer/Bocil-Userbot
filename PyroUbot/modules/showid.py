from PyroUbot import *

__MODULE__ = "showid"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sʜᴏᴡɪᴅ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}id</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> cek id group/channel/user

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}id</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> cek id media/user

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}id</code> [ᴜsᴇʀɴᴀᴍᴇ ᴜsᴇʀ/ɢʀᴜᴘ/ᴄʜᴀɴɴᴇʟ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> cek id 
"""


@PY.UBOT("id", SUDO=False)
async def _(client, message):
    await id_cmd(client, message)
