from .. import *


@PY.UBOT("ping", SUDO=False)
async def _(client, message):
    await ping_cmd(client, message)

@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)
