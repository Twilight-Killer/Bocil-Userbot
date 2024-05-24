from PyroUbot import *

__MODULE__ = "setting"
__HELP__ = """
<b>『 bantuan setting 』</b>

  <b>• perintah:</b> <code>{0}prefix - simbol/emoji</code> 
  <b>• penjelasan:</b> merubah prefix userbot kau 
  
  <b>• perinta:</b> <code>{0}setemoji - [query] [emoji_prem]</code> 
  <b>• query:</b>
         <b>•> pong</b>
         <b>•> uptime</b>
         <b>•> mention</b>
  <b>• penjelasan:</b> merubah tampilan pong uptime dan mention

  <b>• perintah:</b> <code>{0}limit</code>
  <b>• penjelasan:</b> cek status akun 
"""


@PY.BOT("prefix", filters.user(ubot._get_my_id))
@PY.UBOT("prefix")
async def _(client, message):
    await setprefix(client, message)


@PY.UBOT("setemoji")
async def _(client, message):
    await change_emot(client, message)


@PY.UBOT("limit")
async def _(client, message):
    await limit_cmd(client, message)
