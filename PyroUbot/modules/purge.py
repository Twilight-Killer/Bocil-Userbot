from PyroUbot import *

__MODULE__ = "purge"
__HELP__ = """
<b>『 bantuan purger 』</b>

  <b>• perinta:</b> <code>{0}purge</code> [reply to message]
  <b>• penjelasan:</b> hapus sekua obrolan lu

  <b>• perintah:</b> <code>{0}del</code> [reply to message]
  <b>• penjelasan:</b> hapus pesan lu bales

  <b>• perintah:</b> <code>{0}purgeme</code> [nomber to message]
  <b>• penjelasan:</b> hapus pesam lu dengan jumlah hapus
"""


@PY.UBOT("del")
async def _(client, message):
    await del_cmd(client, message)


@PY.UBOT("purgeme")
async def _(client, message):
    await purgeme_cmd(client, message)


@PY.UBOT("purge")
async def _(client, message):
    await purge_cmd(client, message)
