import os
from datetime import timedelta

import wget
from youtubesearchpython import VideosSearch

from PyroUbot import *


async def vsong_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ <b>video tidak ditemukan,</b>\nmohon masuk judul video dengan benar.",
        )
    infomsg = await message.reply_text("<b>🔍 pencarian...</b>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>🔍 pencarian...\n\n{error}</b>")
    try:
        await infomsg.edit("<b>📥 downloader video</b>")
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=True)
    except Exception as error:
        return await infomsg.edit(f"<b>📥 downloader video...\n\n{error}</b>")
    thumbnail_path = None
    file_path = None
    try:
        thumbnail_path = wget.download(thumb)
        file_path = file_name
        await client.send_video(
            message.chat.id,
            video=file_name,
            thumb=thumbnail_path,
            file_name=title,
            duration=duration,
            supports_streaming=True,
            caption=data_ytp.format(
                "ᴠɪᴅᴇᴏ",
                title,
                timedelta(seconds=duration),
                views,
                channel,
                url,
                bot.me.mention,
            ),
            reply_to_message_id=message.id,
        )
    finally:
        if thumbnail_path and os.path.isfile(thumbnail_path):
            os.remove(thumbnail_path)
        if file_path and os.path.isfile(file_path):
            os.remove(file_path)
    await infomsg.delete()


async def song_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ <b>audio tidak ditemukan,</b>\nmohon masuk judul audio dengan benar.",
        )
    infomsg = await message.reply_text("<b>🔍 pencarian...</b>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>🔍 pencarian...\n\n{error}</b>")
    try:
        await infomsg.edit("<b>📥 downloader audio</b>")
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=False)
    except Exception as error:
        return await infomsg.edit(f"<b>📥 downloader audio...\n\n{error}</b>")
    thumbnail_path = None
    file_path = None
    try:
        thumbnail_path = wget.download(thumb)
        file_path = file_name
        await client.send_audio(
            message.chat.id,
            audio=file_name,
            thumb=thumbnail_path,
            file_name=title,
            performer=channel,
            duration=duration,
            caption=data_ytp.format(
                "ᴀᴜᴅɪᴏ",
                title,
                timedelta(seconds=duration),
                views,
                channel,
                url,
                bot.me.mention,
            ),
            reply_to_message_id=message.id,
        )
    finally:
        if thumbnail_path and os.path.isfile(thumbnail_path):
            os.remove(thumbnail_path)
        if file_path and os.path.isfile(file_path):
            os.remove(file_path)
    await infomsg.delete()
