import asyncio
import os

from pyrogram import idle

from PyroUbot import *


async def start_ubot(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=30)
    except asyncio.TimeoutError:
        await remove_ubot(user_id)
        await add_prem(user_id)
        await rm_all(user_id)
        await rem_pref(user_id)
        await remove_all_vars(user_id)
        await rem_uptime(user_id)
        for X in await get_chat(user_id):
            await remove_chat(user_id, X)
        await sending_user(user_id)
        print(f"[𝗜𝗡𝗙𝗢] - ({user_id}) 𝗧𝗜𝗗𝗔𝗞 𝗗𝗔𝗣𝗔𝗧 𝗠𝗘𝗥𝗘𝗦𝗣𝗢𝗡")
    except:
        await remove_ubot(user_id)
        await rm_all(user_id)
        await remove_all_vars(user_id)
        await rem_pref(user_id)
        await rem_uptime(user_id)
        await rem_expired_date(user_id)
        for X in await get_chat(user_id):
            await remove_chat(user_id, X)
        print(f"✅ {user_id} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")


async def main():
    tasks = [
        asyncio.create_task(start_ubot(int(_ubot["name"]), _ubot))
        for _ubot in await get_userbots()
    ]
    await asyncio.gather(*tasks, bot.start())
    await asyncio.gather(loadPlugins(), expiredUserbots(), idle())
    

def loadPlugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), "plugins")
    plugins = [os.path.splitext(f)[0] for f in os.listdir(plugins_dir) if f.endswith(".py") and f != "__init__.py"]
    
    tasks = [
        asyncio.create_task(import_plugin(plugin)) for plugin in plugins
    ]

async def import_plugin(plugin):
    try:
        __import__(f"PyroUbot.plugins.{plugin}")
        print(f"[✅ 𝐋𝐎𝐀𝐃𝐄𝐃] - {plugin}")
    except Exception as e:
        print(f"[❌ 𝐅𝐀𝐈𝐋𝐄𝐃] - {plugin} - {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
