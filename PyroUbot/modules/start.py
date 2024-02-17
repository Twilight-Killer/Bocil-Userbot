from .. import *


@PY.UBOT("ping")
async def ping_cmd(client, message):
    await message.reply_text("_ping")

@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)
