from PyroUbot import *

__MODULE__ = "telegraph"
__HELP__ = """
<b>『 bantuan telegraph 』</b>

  <b>• perintah:</b> <code>{0}tg</code> [reply/media text]
  <b>• penjelasan:</b> untuk meng-upload media/text ke telegraph
"""


@PY.UBOT("tg")
async def _(client, message):
    await tg_cmd(client, message)
