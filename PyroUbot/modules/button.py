from PyroUbot import *

__MODULE__ = "button"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴜᴛᴛᴏɴ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}button</code> text ~> button_text:button_link
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> untuk membuat tombol inline
"""


@PY.UBOT("button")
async def _(client, message):
    await cmd_button(client, message)


@PY.INLINE("^get_button")
@INLINE.QUERY
async def _(client, inline_query):
    await inline_button(client, inline_query)
