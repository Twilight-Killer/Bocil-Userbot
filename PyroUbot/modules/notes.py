from PyroUbot import *

__MODULE__ = "notes"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɴᴏᴛᴇs 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addnote</code> [ɴᴏᴛᴇ_ɴᴀᴍᴇ - ʀᴇᴘʟʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> nyimpan catatan 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}get</code> [ɴᴏᴛᴇ_ɴᴀᴍᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> dapatkan catatan yang di simpan

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delnote</code> [ɴᴏᴛᴇ_ɴᴀᴍᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> hapus catatan

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}notes</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> melihat daftar catatan 

  <b>ɴᴏᴛᴇ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴜᴛᴛᴏɴ, ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ:</b>
  <code>text ~> button_text:button_url</code>
"""


@PY.UBOT("addnote")
async def _(client, message):
    await addnote_cmd(client, message)


@PY.UBOT("get")
async def _(client, message):
    await get_cmd(client, message)


@PY.INLINE("^get_notes")
@INLINE.QUERY
async def _(client, inline_query):
    await get_notes_button(client, inline_query)


@PY.UBOT("delnote")
async def _(client, message):
    await delnote_cmd(client, message)


@PY.UBOT("notes")
async def _(client, message):
    await notes_cmd(client, message)
