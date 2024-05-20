from PyroUbot import *

__MODULE__ = "quotly"
__HELP__ = """
<b>『 bantuan quotly 』</b>

  <b>• perintah:</b> <code>{0}q</code> [reply to text]
  <b>• penjelasan:</b> rubah text jadi stiker

  <b>• perintah:</b> <code>{0}kang</code> [reply to img/stiker]
  <b>• penjelasan:</b> untuk custom stiker/text
"""


@PY.UBOT("q")
async def _(client, message):
    await quotly_cmd(client, message)


@PY.UBOT("kang")
async def _(client, message):
    await kang_cmd(client, message)
