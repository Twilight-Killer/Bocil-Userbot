from PyroUbot import *

__MODULE__ = "profile"
__HELP__ = """
<b>『 bantu profile』</b>

  <b>• perintah:</b> <code>{0}id</code>
  <b>• penjelasan:</b> cek id group/channel/user

  <b>• penjelasan:</b> <code>{0}block</code> [reply user to media]
  <b>• perintah:</b> block chat pribadi

  <b>• perintah:</b> <code>{0}unblock</code> [username/chanel/group]
  <b>• penjelasan:</b> lepas blockiran

  <b>• penjelasan:</b> <code>{0}info</code> [reply user to media]
  <b>• perintah:</b> untuk mendapatkan info pengguna telegram

  <b>• perintah:</b> <code>{0}cinfo</code> [username/chanel/group]
  <b>• penjelasan:</b> untuk mendapatkan info group/channel
"""


@PY.UBOT("id")
async def _(client, message):
    await id_cmd(client, message)


@PY.UBOT("block")
async def _(client, message):
    await block_user(client, message)


@PY.UBOT("unblock")
async def _(client, message):
    await unblock_user(client, message)


@PY.UBOT("info")
async def _(client, message):
    await info_cmd(client, message)


@PY.UBOT("cinfo")
async def _(client, message):
    await cinfo_cmd(client, message)

