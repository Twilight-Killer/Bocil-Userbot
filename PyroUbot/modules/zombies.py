from PyroUbot import *

__MODULE__ = "zombies"
__HELP__ = """
<b>『 bantuan zombies 』</b>

  <b>• perintah:</b> <code>{0}zombies</code>
  <b>• penjelasan:</b> hapus pengguna yang deak di gc lu
"""


@PY.UBOT("zombies", FILTERS.ME_OWNER)
async def _(client, message):
    await zombies_cmd(client, message)
