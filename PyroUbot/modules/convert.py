from PyroUbot import *

__MODULE__ = "convert"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴠᴇʀᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}toanime</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> merubah foto/gif/stiker ke anime

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}toimg</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> merubah stiker/gif ke foto

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tosticker</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> merubah foto ke stiker

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}togif</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>  merubah stiker jadi gif

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}toaudio</code> [ʀᴇᴘʟʏ ᴛᴏ ᴠɪᴅᴇᴏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> mengubah video ke audio 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}efek</code> [ᴇꜰᴇᴋ_ᴄᴏᴅᴇ - ʀᴇᴘʟʏ ᴛᴏ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> untuk mengubah voice note

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}list_efek</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> melihat daftar efek
"""


@PY.UBOT("toanime")
async def _(client, message):
    await convert_anime(client, message)


@PY.UBOT("toimg")
async def _(client, message):
    await convert_photo(client, message)


@PY.UBOT("tosticker")
async def _(client, message):
    await convert_sticker(client, message)


@PY.UBOT("togif")
async def _(client, message):
    await convert_gif(client, message)


@PY.UBOT("toaudio")
async def _(client, message):
    await convert_audio(client, message)


@PY.UBOT("list_efek")
async def _(client, message):
    await list_cmd_efek(client, message)
