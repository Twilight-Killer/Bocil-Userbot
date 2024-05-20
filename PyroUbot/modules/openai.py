from PyroUbot import *

__MODULE__ = "openai"
__HELP__ = """
<b>『 bantuan ai 』</b>

  <b>• perintah:</b> <code>{0}ai</code></code>  [query]
  <b>• penjelasan:</b> pertanyaan ke chatgpt

  <b>• perintah:</b> <code>{0}dalle</code></code> [query]
  <b>• penjelasan:</b> buat foto

  <b>• perintah:</b> <code>{0}stt</code> [reply voice note]
  <b>• penjelasan:</b> merubah pesan menjadi suara desah 
"""


@PY.UBOT("ai")
async def _(client, message):
    await ai_cmd(client, message)


@PY.UBOT("dalle")
async def _(client, message):
    await dalle_cmd(client, message)


@PY.UBOT("stt")
async def _(client, message):
    await stt_cmd(client, message)
