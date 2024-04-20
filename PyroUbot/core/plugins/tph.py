from telegraph import Telegraph, upload_file
from PyroUbot import *


async def tg_cmd(client, message):
    XD = await message.reply("<code>Sedang memproses...</code>")
    if not message.reply_to_message:
        return await XD.edit("<b>Mohon balas ke pesan, untuk mendapatkan link dari Telegraph.</b>")
    
    telegraph = Telegraph()
    telegraph.create_account(short_name='PyroUbot')
    
    if message.reply_to_message.media:
        m_d = await dl_pic(client, message.reply_to_message)
        try:
            media_url = upload_file(m_d)
        except Exception as exc:
            return await XD.edit(f"<code>{exc}</code>")
        u_done = f"<b>Berhasil diupload ke</b> <a href='https://telegra.ph/{media_url}'>Telegraph</a>"
        await XD.edit(u_done)
    elif message.reply_to_message.text:
        page_title = f"{client.me.first_name} {client.me.last_name or ''}"
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except Exception as exc:
            return await XD.edit(f"<code>{exc}</code>")
        wow_graph = f"<b>Berhasil diupload ke</b> <a href='https://telegra.ph/{response['path']}'>Telegraph</a>"
        await XD.edit(wow_graph)
