import asyncio

import aiofiles
import aiohttp
from pyrogram import idle

from PyroUbot.config import YTDLP_COOKIES
from PyroUbot import *


async def write_cookies(url: str, path: str) -> None:
    cookies_string = await get_cookies_file(url=url)
    async with aiofiles.open(path, mode="w") as doc:
        await doc.write(cookies_string)


async def get_cookies_string(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()

        return content


async def start_ubot(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=30)
    except asyncio.TimeoutError:
        await handle_timeout_error(user_id)
    except Exception as e:
        await handle_generic_error(user_id, e)


async def handle_timeout_error(user_id):
    await remove_ubot(user_id)
    await add_prem(user_id)
    await rm_all(user_id)
    await rem_pref(user_id)
    await remove_all_vars(user_id)
    await rem_uptime(user_id)
    for X in await get_chat(user_id):
        await remove_chat(user_id, X)
    await sending_user(user_id)
    logger.info(f"({user_id})  𝗧𝗜𝗗𝗔𝗞 𝗗𝗔𝗣𝗔𝗧 𝗠𝗘𝗥𝗘𝗦𝗣𝗢𝗡")


async def handle_generic_error(user_id, error):
    await remove_ubot(user_id)
    await rm_all(user_id)
    await remove_all_vars(user_id)
    await rem_pref(user_id)
    await rem_uptime(user_id)
    await rem_expired_date(user_id)
    for X in await get_chat(user_id):
        await remove_chat(user_id, X)
    logger.info(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦: {error}")


async def main():
    await bot.start()

    ubots = await get_userbots()
    for ubot in ubots:
        await start_ubot(int(ubot["name"]), ubot)

    await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots())

    if YTDLP_COOKIES:
        await write_cookies(url=YTDL_COOKIES, path="./storage/cookies.txt")

    await idle()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(main())
