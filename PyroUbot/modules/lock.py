from PyroUbot import *


__MODULE__ = "locks"
__HELP__ = f"""
<b>『 bantuan locks』</b>

  <b>• perintah:</b> <code>{0}info</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀs]
  <b>• penjelasan:</b> mendapatkan info pengguna di lengkapi 

  <b>• perintah:</b> <code>{0}cinfo</code> [chat_id/username/reply to chat]
  <b>• penjelasan:</b> untuk mendapatkan info pengguna
  
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


@PY.UBOT("info")
async def _(client, message):
    await info_cmd(client, message)


@PY.UBOT("cinfo")
async def _(client, message):
    await cinfo_cmd(client, message)
