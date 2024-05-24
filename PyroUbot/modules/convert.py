from PyroUbot import *

__MODULE__ = "convert"
__HELP__ = """
<b>『 bantuan conver 』</b>

  <b>• perinta:</b> <code>{0}toanime</code> [reply to foto/stiker/text]
  <b>• penjelasan:</b> merubah foto/gif/stiker ke anime

  <b>• perintah:</b> <code>{0}toimg</code> [reply to stiker/gif]
  <b>• penjelasan:</b> merubah stiker/gif ke foto

  <b>• perintah:</b> <code>{0}tosticker</code> [reply to foto]
  <b>• penjelasan:</b> merubah foto ke stiker

  <b>• perintah:</b> <code>{0}togif</code> [reply to stiker]
  <b>• penjelasan:</b>  merubah stiker jadi gif

  <b>• perintah:</b> <code>{0}toaudio</code> [reply to video]
  <b>• penjelasan:</b> mengubah video ke audio 

  <b>• perintah:</b> <code>{0}efek</code> [list efek suara]
  <b>• penjelasan:</b> untuk mengubah voice note

  <b>• perintah:</b> <code>{0}list_efek</code>
  <b>• penjelasan:</b> melihat daftar efek
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
