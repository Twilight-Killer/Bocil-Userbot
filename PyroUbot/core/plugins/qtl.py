import asyncio
import os

from pyrogram.raw.functions.messages import DeleteHistory


async def quotly_cmd(client, message):
    info = await message.reply("<b>ᴍᴇᴍᴘʀᴏsᴇs.....</b>", quote=True)
    await client.unblock_user("@QuotLyBot")
    if message.reply_to_message:
        if len(message.command) < 2:
            msg = [message.reply_to_message]
        else:
            try:
                count = int(message.command[1])
            except ValueError as error:
                return await info.edit(str(error))
            msg = [
                i
                for i in await client.get_messages(
                    chat_id=message.chat.id,
                    message_ids=range(
                        message.reply_to_message.id, message.reply_to_message.id + count
                    ),
                    replies=-1,
                )
            ]
        try:
            for x in msg:
                await x.forward("@QuotLyBot")
        except Exception as error:
            return await info.edit(str(error))

        await asyncio.sleep(9)
        await info.delete()
        async for quotly in client.iter_history("@QuotLyBot", limit=1):
            if not quotly.sticker:
                return await message.reply(
                    "❌ @QuotLyBot ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇʀᴇsᴘᴏɴ ᴘᴇʀᴍɪɴᴛᴀᴀɴ", quote=True
                )

            sticker = await quotly.download()
            await message.reply_sticker(sticker, quote=True)
            os.remove(sticker)
    else:
        if len(message.command) < 2:
            return await info.edit("<b>ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ</b>")
        else:
            msg = await client.send_message(
                "@QuotLyBot", f"/qcolor {message.command[1]}"
            )
            await asyncio.sleep(1)
            get = await msg.reply_to_message
            await info.edit(
                f"<b>ᴡᴀʀɴᴀ ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ᴋᴜᴛɪᴘᴀɴ ᴅɪsᴇᴛᴇʟ ᴋᴇ:</b> <code>{get.text.split(':')[1]}</code>"
            )

    user_info = await client.resolve_peer("@QuotLyBot")
    return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))

    # Balasan juga dikirim kembali ke grup atau pengguna yang memicu perintah
    await message.reply("Pesannya telah diteruskan ke grup atau pengguna lain.")
