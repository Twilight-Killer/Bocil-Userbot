import asyncio
from pyrogram.raw.functions.messages import DeleteHistory

async def sosmed_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(
            "<code>Harap sertakan link yt/ig/fb/tw/tiktok.</code>"
        )

    bot = "msaver_bot"
    link = message.command[1]
    await client.unblock_user(bot)
    Tm = await message.reply("<code>proses...</code>")

    try:
        # Kirim link ke bot
        xnxx = await client.send_message(bot, link)
        await asyncio.sleep(10)
        
        # Ambil respons dari bot
        sosmed = await client.get_messages(bot, xnxx.id + 2)

        if sosmed and sosmed.media:
            # Unduh media dari respons bot
            media_path = await sosmed.download()
            if media_path:
                # Kirim media yang diunduh ke chat asal dengan mereply pesan asli
                await client.send_message(
                    chat_id=message.chat.id,
                    caption=sosmed.caption,
                    reply_to_message_id=message.id,
                    file=media_path
                )
                await Tm.delete()
            else:
                await Tm.edit("<b>Gagal mengunduh media.</b>")
        else:
            await Tm.edit("<b>Tidak ada media dalam respons.</b>")

    except Exception as e:
        await Tm.edit(f"<b>Kesalahan: {str(e)}</b>")
    
    finally:
        # Hapus riwayat percakapan dengan bot
        user_info = await client.resolve_peer(bot)
        await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
