from PyroUbot import *


__MODULE__ = "locks"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏᴄᴋꜱ 』</b>

  <b>• perintah:</b> <code>{0}lock</code> [type]
  <b>• penjelasan:</b> mengkunci izin group 

  <b>• perintah:</b> <code>{0}unlock</code> [type]
  <b>• penjelasan:</b> buka izin grouo

  <b>• perintah:</b> <code>{0}locks</code>
  <b>• penjelasan:</b> cek izin group

  <b>• type : `msg`|`media`|`stickers`|`polls`|`info`|`invite`|`webprev`|`pin`
"""


@PY.UBOT("lock|unlock")
async def _(client, message):
    await locks_func(client, message)


@PY.UBOT("locks")
async def _(client, message):
    await locktypes(client, message)
