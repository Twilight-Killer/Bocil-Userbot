from .. import *


@PY.UBOT("ping")
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)


@PY.CALLBACK("stats")
async def _(client, callback_query):
    await callback_query_halder(client, callback_query)


@PY.CALLBACK("refresh")
async def _(client, callback_query):
    await callback_query_refresh(client, callback_query)
