from PyroUbot import *

__MODULE__ = "youtube"
__HELP__ = """
<b>『 bantuan youtube 』</b>

  <b>• perintah:</b> <code>{0}song</code> [song title]
  <b>• penjelasan:</b> download music lu pengen 

  <b>• perintah:</b> <code>{0}vsong</code> [song title]
  <b>• penjelasan:</b> download video lu pengen 
"""


@PY.UBOT("vsong")
async def _(client, message):
    await vsong_cmd(client, message)


@PY.UBOT("song")
async def _(client, message):
    await song_cmd(client, message)
