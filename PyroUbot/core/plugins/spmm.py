import asyncio

dspam_processes = {}  # Dictionary to store information about dspam processes

async def spam_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("Sedang diproses", quote=False)
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
            return await msg.edit("Silakan ketik <code>.help spam</code> untuk melihat cara menggunakan perintah ini")
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
    msg = await message.reply("Sedang diproses", quote=False)
    if reply:
        try:
            count_message = int(message.command[1])
            count_delay = int(message.command[2])
        except Exception as error:
            return await msg.edit(str(error))
        dspam_processes[message.chat.id] = {"count_message": count_message, "count_delay": count_delay, "text_spam": reply.text}
        for i in range(count_message):
            try:
                await reply.copy(message.chat.id)
                await asyncio.sleep(count_delay)
            except:
                pass
        dspam_processes.pop(message.chat.id, None)
    else:
        if len(message.command) < 4:
            return await msg.edit("Silakan ketik <code>.help spam</code> untuk melihat cara menggunakan perintah ini")
        else:
            try:
                count_message = int(message.command[1])
                count_delay = int(message.command[2])
            except Exception as error:
                return await msg.edit(str(error))
            dspam_processes[message.chat.id] = {"count_message": count_message, "count_delay": count_delay, "text_spam": message.text.split(None, 3)[3]}
            for i in range(count_message):
                try:
                    await message.reply(message.text.split(None, 3)[3], quote=False)
                    await asyncio.sleep(count_delay)
                except:
                    pass
            dspam_processes.pop(message.chat.id, None)
    await msg.delete()
    await message.delete()

async def list_dspam(client, message):
    if not dspam_processes:
        return await message.reply("Tidak ada proses dspam yang sedang berjalan.")
    text = "Proses dspam sedang berjalan di grup ini:\n"
    for chat_id, process_info in dspam_processes.items():
        text += f"- {chat_id} (Penundaan: {process_info['count_delay']} detik, Kata-kata: {process_info['text_spam']})\n"
    await message.reply(text)

async def cancel_dspam(client, message):
    if message.chat.id not in dspam_processes:
        return await message.reply("Tidak ada proses dspam yang sedang berjalan di grup ini.")
    dspam_processes.pop(message.chat.id, None)
    await message.reply("Proses dspam berhasil dibatalkan.")

async def addtext_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("Silakan berikan kata-kata yang ingin ditambahkan.")
    
    new_text = ' '.join(message.command[1:])
    if message.chat.id in dspam_processes:
        dspam_processes[message.chat.id]["text_spam"] += f" {new_text}"
        return await message.reply(f"Kata-kata '{new_text}' berhasil ditambahkan ke dalam proses dspam.")
    else:
        return await message.reply("Tidak ada proses dspam yang sedang berjalan di grup ini.")
