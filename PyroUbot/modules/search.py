from PyroUbot import *

__MODULE__ = "search"
__HELP__ = """
<b>『 bantuan search 』</b>

  <b>• perintah:</b> <code>{0}pic</code> [query]
  <b>• penjelasan:</b> cari foto random dari gogle

  <b>• perintah:</b> <code>{0}gif</code> [query]
  <b>• penjelasan:</b> cari gif
"""


@PY.UBOT("pic")
async def _(client, message):
    await pic_bing_cmd(client, message)


@PY.UBOT("bing")
async def _(client, message):
    await pic_bing_cmd(client, message)


@PY.UBOT("gif")
async def _(client, message):
    await gif_cmd(client, message)
