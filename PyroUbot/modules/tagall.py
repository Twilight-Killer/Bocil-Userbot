from PyroUbot import *

__MODULE__ = "all&$spam"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴀɢᴀʟʟ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tagall</code> [ᴛʏᴘᴇ ᴍᴇssᴀɢᴇ/ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ] 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ngetag semua anggota group

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}batal</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> mematikan ngetag

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}spam</code> [ᴊᴜᴍʟᴀʜ_ᴘᴇsᴀɴ - ᴘᴇsᴀɴ_sᴘᴀᴍ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ sᴘᴀᴍ ᴘᴇsᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}dspam</code> [ᴊᴜᴍʟᴀʜ_ᴘᴇsᴀɴ - ᴊᴜᴍʟᴀʜ_ᴅᴇʟᴀʏ_ᴅᴇᴛɪᴋ - ᴘᴇsᴀɴ_sᴘᴀᴍ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> untuk spam pesan delay

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}spmlist</code> 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> melihat list dspam

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}henti</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> menghentikan dspam

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ddtext</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> menambahkan text dspam
"""


@PY.UBOT("tagall")
async def _(client, message):
    await tagall_cmd(client, message)


@PY.UBOT("batal")
async def _(client, message):
    await batal_cmd(client, message)


@PY.UBOT("spam")
async def _(client, message):
    await spam_cmd(client, message)


@PY.UBOT("dspam")
async def _(client, message):
    await dspam_cmd(client, message)


@PY.UBOT("spmlist")
async def _(client, message):
    await list_dspam(client, message)


@PY.UBOT("henti")
async def _(client, message):
    await cancel_dspam(client, message)


@PY.UBOT("ddtext")
async def _(client, message):
    await addtext_cmd (client, message)
