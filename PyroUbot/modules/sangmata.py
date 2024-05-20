from PyroUbot import *

__MODULE__ = "sangmata"
__HELP__ = """
<b>『 bantuan sangmata 』</b>

  <b>• perintah:</b> <code>{0}sg</code> [user_id/reply]
  <b>• penjelasan:</b> cek histori orang
"""


@PY.UBOT("sg")
async def _(client, message):
    await sg_cmd(client, message)
