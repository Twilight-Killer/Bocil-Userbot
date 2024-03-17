from PyroUbot import *

MODULE = "sosmed"
HELP = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴏsᴍᴇᴅ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}sosmed</code> [ʟɪɴᴋ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴅᴀʀɪ ꜰᴀᴄᴇʙᴏᴏᴋ/ᴛɪᴋᴛᴏᴋ/ɪɴsᴛᴀɢʀᴀᴍ/ᴛᴡɪᴛᴛᴇʀ/ʏᴏᴜᴛᴜʙᴇ
"""


@PY.UBOT("sosmed")
async def _(client, message):
    await sosmed_cmd(client, message)
