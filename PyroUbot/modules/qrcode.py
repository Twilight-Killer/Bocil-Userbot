from PyroUbot import *

__MODULE__ = "qrcode"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ǫʀᴄᴏᴅᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}qrGen</code> [ᴛᴇxᴛ ǫʀᴄᴏᴅᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> rubah qrcode text ke gambar 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}qrRead</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> rubah qrcode jadi text
"""


@PY.UBOT("qrgen")
async def _(client, message):
    await qr_gen_cmd(client, message)


@PY.UBOT("qrread")
async def _(client, message):
    await qr_read_cmd(client, message)
