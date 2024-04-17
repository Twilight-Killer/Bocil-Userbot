import asyncio

spam_id = []
dspam_id = []

async def spam_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs", quote=False)
    if reply:
        try:
            count_message = int(message.command[1])
            for i in range(count_message):
                await reply.copy(message.chat.id)
                await asyncio.sleep(0.1)
        except Exception as error:
            return await msg.edit(str(error))
    else:
        if len(message.command) < 2:
            return await msg.edit(
                "sɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ <code>.help spam</code> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ"
            )
        else:
            try:
                count_message = int(message.command[1])
                for i in range(count_message):
                    await message.reply(message.text.split(None, 2)[2], quote=False)
                    await asyncio.sleep(0.1)
            except Exception as error:
                return await msg.edit(str(error))
    await msg.delete()
    await message.delete()


async def dspam_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs", quote=False)
    if reply:
        try:
            count_message = int(message.command[1])
            count_delay = int(message.command[2])
        except Exception as error:
            return await msg.edit(str(error))
        dspam_id.append(message.chat.id)
        for i in range(count_message):
            try:
                await reply.copy(message.chat.id)
                await asyncio.sleep(count_delay)
            except:
                pass
        dspam_id.remove(message.chat.id)
    else:
        if len(message.command) < 4:
            return await msg.edit(
                "sɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ <code>.help spam</code> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ"
            )
        else:
            try:
                count_message = int(message.command[1])
                count_delay = int(message.command[2])
            except Exception as error:
                return await msg.edit(str(error))
            dspam_id.append(message.chat.id)
            for i in range(count_message):
                try:
                    await message.reply(message.text.split(None, 3)[3], quote=False)
                    await asyncio.sleep(count_delay)
                except:
                    pass
            dspam_id.remove(message.chat.id)
    await msg.delete()
    await message.delete()


async def list_dspam(client, message):
    if not dspam_id:
        return await message.reply("Tidak ada proses dspam yang sedang berjalan.")
    text = "Proses dspam sedang berjalan di grup ini:\n"
    for chat_id, _, count_message, count_delay, text_spam in dspam_id:
        try:
            chat = await client.get_chat(chat_id)
            text += f"- {chat.title} (Penundaan: {count_delay} detik, Kata-kata: {text_spam})\n"
        except:
            pass
    await message.reply(text)


async def cancel_dspam(client, message):
    if message.chat.id not in dspam_id:
        return await message.reply("Tidak ada proses dspam yang sedang berjalan di grup ini.")
    dspam_id.remove(message.chat.id)
    await message.reply("Proses dspam berhasil dibatalkan.")


async def addtext_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("Silakan berikan kata-kata yang ingin ditambahkan.")
    
    new_text = ' '.join(message.command[1:])
    for i, (chat_id, _, _, _, old_text) in enumerate(dspam_id):
        if chat_id == message.chat.id:
            dspam_id[i] = (chat_id, _, _, _, old_text + f" {new_text}")
            break
    else:
        return await message.reply("Tidak ada proses dspam yang sedang berjalan di grup ini.")
    
    return await message.reply(f"Kata-kata '{new_text}' berhasil ditambahkan ke dalam proses dspam.")
