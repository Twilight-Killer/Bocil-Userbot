from PyroUbot import *

__MODULE__ = "translate&tiny"
__HELP__ = """
<b>『 bantuan translate  』</b>

  <b>• perintah:</b> <code>{0}tr</code> [reply/text]
  <b>• penjelasan:</b> terjemahah bahasa

  <b>• perintah:</b> <code>{0}tts</code> [reply/text]
  <b>• penjelasan:</b> rubah tect ke suara

  <b>• perintah:</b> <code>{0}set_lang</code>
  <b>• penjelasan:</b> rubah bahasa terjemahan 

  <b>• perintah:</b> <code>{0}tiny</code> [reply to stiker]
  <b>• penjelasan:</b> rubah stiker jadi kecil
"""


@PY.UBOT("tts")
async def _(client, message):
    await tts_cmd(client, message)


@PY.UBOT("tr")
async def _(client, message):
    await tr_cmd(client, message)


@PY.UBOT("set_lang")
async def _(client, message):
    await set_lang_cmd(client, message)


@PY.INLINE("^ubah_bahasa")
@INLINE.QUERY
async def _(client, inline_query):
    await ubah_bahasa_inline(client, inline_query)


@PY.CALLBACK("^set_bahasa")
@INLINE.DATA
async def _(client, callback_query):
    await set_bahasa_callback(client, callback_query)


@PY.UBOT("tiny")
async def _(client, message):
    await tiny_cmd(client, message)
