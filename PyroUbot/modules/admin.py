from PyroUbot import *

__MODULE__ = "admin"
__HELP__ = """
<b>『 bantuan untuk admin 』</b>

  <b>• perinta:</b> <code>{0}kick</code> [user_id/username/reply]
  <b>• penjelasan:</b> menendang member rasis 

  <b>• perinta:</b> <code>{0}ban</code> 
  <b>• penjelasan:</b> ban member rasis

  <b>• perinta:</b> <code>{0}mute</code>
  <b>• penjelasan:</b> membisukan member

  <b>• perinta:</b> <code>{0}unmute</code>
  <b>• penjelasan:</b> lepas bisukan member

  <b>• perinta:</b> <code>{0}unban</code>
  <b>• penjelasan:</b> lepas ban dari group lu

  <b>• perinta:</b> <code>{0}staff</code>
  <b>• penjelasan:</b> lihat daftar admin di group
"""


@PY.UBOT("kick|dkick", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_kick(client, message)


@PY.UBOT("ban|dban", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_ban(client, message)


@PY.UBOT("mute|dmute", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_mute(client, message)


@PY.UBOT("unmute", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_unmute(client, message)


@PY.UBOT("unban", FILTERS.ME_GROUP)
async def _(client, message):
    await admin_unban(client, message)


@PY.UBOT("staff")
async def _(client, message):
    await staff_cmd(client, message)
