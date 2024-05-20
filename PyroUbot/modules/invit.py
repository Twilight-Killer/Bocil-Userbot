from PyroUbot import *

__MODULE__ = "invite"
__HELP__ = """
<b>『 bantuan invit 』</b>

  <b>• perintah:</b> <code>{0}invite</code> [ᴜsᴇʀɴᴀᴍᴇ] 
  <b>• penjelasan:</b> mengundang anggota kegroup lu

  <b>• perintah:</b> <code>{0}inviteall</code> [username_group- colldown=detik per invit]
  <b>• penjelasan:</b> mengundang anggota

  <b>• perintah:</b> <code>{0}cancel</code>
  <b>• penjelasan:</b> membatalkan invitall
  """


@PY.UBOT("invite")
async def _(client, message):
    await invite_cmd(client, message)


@PY.UBOT("inviteall")
async def _(client, message):
    await inviteall_cmd(client, message)


@PY.UBOT("cancel")
async def _(client, message):
    await cancel_cmd(client, message)
