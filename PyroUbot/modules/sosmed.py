from PyroUbot import *

__MODULE__ = "sosmed"
__HELP__ = """
<b>『 bantuan sosmed 』</b>

  <b>• perintah:</b> <code>{0}sosmed</code> [link]
  <b>• penjelasan:</b> download vidio /fb/ig/yt/all in
"""


@PY.UBOT("sosmed")
async def _(client, message):
    await sosmed_cmd(client, message)
