from asyncio import sleep
from pyrogram import raw
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

async def limit_cmd(client, message):
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await message.reply("<code>ᴘʀᴏᴄᴇssɪɴɢ . . .</code>")
    
    start_bot = raw.functions.messages.StartBot(
        bot=bot_info,
        peer=bot_info,
        random_id=client.rnd_id(),
        start_param="start"
    )
    
    response = await client.send(start_bot)
    await sleep(1)
    await msg.delete()
    
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1)
    await status.copy(message.chat.id, reply_to_message_id=message.message_id)
    
    delete_history = raw.functions.messages.DeleteHistory(peer=bot_info, max_id=0, revoke=True)
    return await client.send(delete_history)
