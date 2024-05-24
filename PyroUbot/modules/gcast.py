from PyroUbot import *

__MODULE__ = "gcast"
__HELP__ = """
<b>『 bantuan gcast 』</b>

  <b>• perintah:</b> <code>{0}ucast</code> [text/reply to text/media]
  <b>• penjelasan:</b> mengirim pesan ke chat 

  <b>• perintah:</b> <code>{0}gcast</code> [text/reply to text/media]
  <b>• penjelasan:</b> mengirim pesan ke group 

  <b>• perintah:</b> <code>{0}send</code> [userid/username to reply/text]
  <b>• penjelasan:</b> mengirim pesan ke group channel chat

    <b>• perintah:</b> auto_gcast (qury) - (value)
      <b>•> query & value:</b>
        <b>on/off:</b> untuk aktifkan dan nonaktifkan auto_gcast
        <b>text - kata-kata/reply_text:<b> menambahkan kata kata ke database
        <b>delay - angka:</b> merubah delay auto gcast
        <b>limit - on/off:</b> aktif/non-aktif untuk cek limit 15 menit sekali
  <b>• penjelasan:</b> mengerim pesan gcast otomatis 

  <b>• perintah:</b> <code>{0}gban</ᴄᴏᴅᴇ> [userid/username to reply/user]
  <b>• penjelasan:</b> banned pengguna 

  <b>• perintah:</b> <code>{0}ungban</code> [user_id/username to reply/user]
  <b>• penjelasan:</b> unban pengguna 
"""


@PY.UBOT("gcast")
async def _(client, message):
    await broadcast_group_cmd(client, message)


@PY.UBOT("ucast")
async def _(client, message):
    await broadcast_users_cmd(client, message)


@PY.BOT("send")
@PY.UBOT("send")
async def _(client, message):
    await send_msg_cmd(client, message)


@PY.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)


@PY.UBOT("gban")
async def _(client, message):
    await global_banned(client, message)


@PY.UBOT("ungban")
async def _(client, message):
    await global_unbanned(client, message)
  

AG = []
LT = []


@PY.UBOT("auto_gcast")
async def _(client, message):
    msg = await message.reply("<b>prosesss....</b>", quote=True)
    type, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT")

    if type == "on":
        if not auto_text_vars:
            return await msg.edit(
                "<b>harap setting text gcast anda dahulu </b>"
            )

        if client.me.id not in AG:
            await msg.edit("<b>auto gcast diaktifkan</b>")

            AG.append(client.me.id)

            done = 0
            while client.me.id in AG:
                delay = await get_vars(client.me.id, "DELAY_GCAST") or 1
                blacklist = await get_chat(client.me.id)
                txt = random.choice(auto_text_vars)

                group = 0
                async for dialog in client.get_dialogs():
                    if (
                        dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
                        and dialog.chat.id not in blacklist
                    ):
                        try:
                            await asyncio.sleep(1)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except Exception:
                            pass

                if client.me.id not in AG:
                    return

                done += 1
                await msg.reply(
                    f"<b>auto gcast putaran {done} berhasil terkirim ke: {group} group\n\nmenunggu {delay} menit lagi untuk mengirim pesan selanjutnya</b>",
                    quote=True,
                )
                await asyncio.sleep(int(60 * int(delay)))
        else:
            return await msg.delete()

    elif type == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit("<b>auto gcast di non-aktifkan</b>")
        else:
            return await msg.delete()

    elif type == "text":
        if not value:
            return await msg.edit(
                "<b>masukan text auto gcast untuk di gcast kan</b>"
            )
        await add_auto_text(client, value)
        return await msg.edit("<b>auto gcast text: berhasil disimpan</b>")

    elif type == "delay":
        await set_vars(client.me.id, "DELAY_GCAST", value)
        return await msg.edit(
            f"<b>auto gcast delay: berhasil setting ke {value} menit</b>"
        )

    elif type == "remove":
        if not value:
            return await msg.edit(
                "<b>masukan angka untuk menghapus list text</b>"
            )
        if value == "all":
            await set_vars(client.me.id, "AUTO_TEXT", [])
            return await msg.edit("<b>semua text berhasil dihapus</b>")
        try:
            value = int(value) - 1
            auto_text_vars.pop(value)
            await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
            return await msg.edit(
                f"<b>auto gcast remove: text ke {value+1} berhasil dihapus\n\nsilahkan ketik: <code>{message.text.split()[0]} list</code>, kembali untuk mengecek apa sudah terhapus</b>"
            )
        except Exception as error:
            return await msg.edit(str(error))

    elif type == "list":
        if not auto_text_vars:
            return await msg.edit("<b>auto gcast text kosong</b>")
        txt = "<b>ᴅᴀғᴛᴀʀ ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ</b>\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"{num}: {x}\n\n"
        txt += f"<b>\nuntuk menghapus text ketik: <code>{message.text.split()[0]} remove angka/all</code></b>"
        return await msg.edit(txt)

    elif type == "limit":
        if value == "off":
            if client.me.id in LT:
                LT.remove(client.me.id)
                return await msg.edit("<b>auto cek limit dinonaktifkan</b>")
            else:
                return await msg.delete()

        elif value == "on":
            if client.me.id not in LT:
                LT.append(client.me.id)
                await msg.edit("<b>auto cek limit started</b>")
                while client.me.id in LT:
                    for x in range(2):
                        await spam_bot(client, message)
                        await asyncio.sleep(5)
                    await asyncio.sleep(1200)
            else:
                return await msg.delete()
        else:
             return await msg.edit("<b>~harap masukan value on/off untuk menggunakan perinta ini</b>")
    else:
        return await msg.edit("<b>query sayang dimasukan salah</b>")


async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)


def extract_type_and_text(message):
    args = message.text.split(None, 2)
    if len(args) < 2:
        return None, None

    type = args[1]
    msg = (
        message.reply_to_message.text
        if message.reply_to_message
        else args[2]
        if len(args) > 2
        else None
    )
    return type, msg
