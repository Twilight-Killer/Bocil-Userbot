import asyncio

from pyrogram.raw.functions.messages import DeleteHistory


async def sosmed_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(
            f"<code>{message.text}</code> link yt/ig/fb/tw/tiktok"
        )
    else:
        bot = "msaver_bot"
        link = message.text.split()[1]
        await client.unblock_user(bot)
        Tm = await message.reply("<code>proses...</code>")
        xnxx = await client.send_message(bot, link)
        await asyncio.sleep(10)
        try:
            sosmed = await client.get_messages(bot, xnxx.id + 2)
            media = await sosmed.download()
            if media:
                await client.send_message(
                    chat_id=message.chat.id,
                    caption=sosmed.caption,
                    reply_to_message_id=message.id,
                    file=media
                )
            await Tm.delete()
        except Exception as e:
            await Tm.edit(
                "<b>Video tidak ditemukan. Silakan coba lagi beberapa saat lagi.</b>"
            )
        user_info = await client.resolve_peer(bot)
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
