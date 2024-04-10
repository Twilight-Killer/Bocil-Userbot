from PyroUbot import *

__MODULE__ = "convert"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴠᴇʀᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}toanime</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ ᴍᴇɴᴊᴀᴅɪ ɢᴀᴍʙᴀʀ ᴀɴɪᴍᴇ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}toimg</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ ᴍᴇɴᴊᴀᴅɪ ᴘʜᴏᴛᴏ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tosticker</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ꜰᴏᴛᴏ ᴍᴇɴᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}togif</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>  ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ sᴛɪᴄᴋᴇʀ ᴍᴇɴᴊᴀᴅɪ ɢɪꜰ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}toaudio</code> [ʀᴇᴘʟʏ ᴛᴏ ᴠɪᴅᴇᴏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴠɪᴅᴇᴏ ᴍᴇɴᴊᴀᴅɪ ᴀᴜᴅɪᴏ ᴍᴘ3

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}efek</code> [ᴇꜰᴇᴋ_ᴄᴏᴅᴇ - ʀᴇᴘʟʏ ᴛᴏ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ sᴜᴀʀᴀ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}list_efek</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀғᴛᴀʀ ᴇғᴇᴋ
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
