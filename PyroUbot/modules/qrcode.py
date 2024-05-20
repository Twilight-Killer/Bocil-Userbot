from PyroUbot import *

__MODULE__ = "qrcode"
__HELP__ = """
<b>『 bantuan qrcode 』</b>

  <b>• perintah:</b> <code>{0}qrGen</code> [text qrcode]
  <b>• penjelasan:</b> rubah qrcode text ke gambar 

  <b>• perintah:</b> <code>{0}qrRead</code> [reply to media]
  <b>• penjelasan:</b> rubah qrcode jadi text
"""


@PY.UBOT("qrgen")
async def _(client, message):
    await qr_gen_cmd(client, message)


@PY.UBOT("qrread")
async def _(client, message):
    await qr_read_cmd(client, message)
