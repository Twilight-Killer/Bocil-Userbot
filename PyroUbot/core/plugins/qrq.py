import asyncio
import os

import requests
from bs4 import BeautifulSoup


async def qr_gen_cmd(client, message):
    ID = message.reply_to_message or message
    if message.reply_to_message:
        data = qr_gen(message.reply_to_message.text)
    else:
        if len(message.command) < 2:
            return await message.delete()
        else:
            input_text = message.text.split(None, 1)[1]
            if len(input_text) > 1000:
                return await message.reply("Input terlalu panjang.")
            data = qr_gen(input_text)
    Tm = await message.reply("sedang prosen qrcode....")
    try:
        QRcode = (
            requests.post(
                "https://api.qrcode-monkey.com//qr/custom",
                json=data,
            )
            .json()["imageUrl"]
            .replace("//api", "https://api")
        )
        await client.send_photo(message.chat.id, QRcode, reply_to_message_id=ID.message_id)
        await Tm.delete()
    except Exception as error:
        await Tm.edit(str(error))


async def qr_read_cmd(client, message):
    replied = message.reply_to_message
    if not (replied and replied.media and (replied.photo or replied.sticker)):
        await message.reply("balas qr untuk mendapatkan data...")
        return
    if not os.path.isdir("premiumQR/"):
        os.makedirs("premiumQR/")
    AM = await message.reply("mengundu mediaa...")
    down_load = await client.download_media(message=replied, file_name="premiumQR/")
    await AM.edit("proses kodr qr anda...")
    cmd = [
        "curl",
        "-X",
        "POST",
        "-F",
        "f=@" + down_load + "",
        "https://zxing.org/w/decode",
    ]
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    out_response = stdout.decode().strip()
    err_response = stderr.decode().strip()
    os.remove(down_load)
    if not (out_response or err_response):
        await AM.edit("tida bisa mendapatkan data kode qr anda...")
        return
    try:
        soup = BeautifulSoup(out_response, "html.parser")
        qr_contents = soup.find_all("pre")[0].text
    except IndexError:
        await AM.edit("indeks daftar diluar jangkauan")
        return
    await AM.edit(f"<b>data qrcode:</b>\n<code>{qr_contents}</code>")
