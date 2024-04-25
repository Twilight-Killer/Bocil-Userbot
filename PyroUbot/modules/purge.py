from PyroUbot import *

__MODULE__ = "purge"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴜʀɢᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}purge</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> hapus sekua obrolan lu

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}del</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> hapus pesan lu bales

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}purgeme</code> [ɴᴜᴍʙᴇʀ ᴏꜰ ᴍᴇssᴀɢᴇs]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> hapus pesam lu dengan jumlah hapus
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
