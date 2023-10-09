from pyrogram.enums import ChatType

from PyroUbot import OWNER_ID, bot, ubot


async def install_my_peer(client):
    pm_chats, gc_chats = await get_private_and_group_chats(client)
    client_id = client.me.id
    client._get_my_peer[client_id] = {"pm": pm_chats, "gc": gc_chats}


async def installPeer():
    try:
        for client in ubot._ubot:
            await install_my_peer(client)
    except Exception:
        pass
    await bot.send_message(OWNER_ID, "✅ sᴇᴍᴜᴀ ᴘᴇᴇʀ_ɪᴅ ʙᴇʀʜᴀsɪʟ ᴅɪɪɴsᴛᴀʟʟ")
