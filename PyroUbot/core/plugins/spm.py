import asyncio
from datetime import datetime, timedelta
from contextlib import suppress

import pytz

from PyroUbot import *

dspam_processes = {}


async def spam_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("Sedang diproses", quote=False)
    try:
        if len(message.command) < 2:
            await msg.edit(
                "Silakan ketik <code>.help spam</code> untuk melihat cara menggunakan perintah ini"
            )
            return

        count_message = int(message.command[1])

        if reply:
            for i in range(count_message):
                await reply.copy(message.chat.id)
                await asyncio.sleep(0.1)
        else:
            if len(message.command) < 3:
                await msg.edit("Silakan masukkan teks untuk spam.")
                return

            text_to_send = message.text.split(None, 2)[2]
            for i in range(count_message):
                await message.reply(text_to_send, quote=False)
                await asyncio.sleep(0.1)
    except ValueError:
        await msg.edit("Silakan masukkan jumlah pesan yang valid.")
    except Exception as error:
        await msg.edit(str(error))
    finally:
        with suppress(Exception):
            await msg.delete()
            await message.delete()


async def dspam_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("Sedang diproses", quote=False)
    try:
        if len(message.command) < 3:
            await msg.edit(
                "Silakan ketik <code>.help dspam</code> untuk melihat cara menggunakan perintah ini"
            )
            return

        count_message = int(message.command[1])
        count_delay = int(message.command[2])

        wib_timezone = pytz.timezone("Asia/Jakarta")
        now = datetime.now(wib_timezone)

        if len(message.command) > 3:
            scheduled_time = message.command[3]
            try:
                scheduled_dt = datetime.strptime(scheduled_time, "%H:%M")
                scheduled_dt = scheduled_dt.replace(
                    year=now.year, month=now.month, day=now.day
                )
                scheduled_dt = wib_timezone.localize(scheduled_dt)

                if scheduled_dt < now:
                    scheduled_dt += timedelta(days=1)
                delay_until_start = (scheduled_dt - now).total_seconds()
            except ValueError:
                await msg.edit("Silakan masukkan waktu yang valid dalam format HH:MM.")
                return
        else:
            delay_until_start = 0

        if reply:
            text_spam = reply.text
        else:
            if len(message.command) < 5:
                await msg.edit("Silakan masukkan teks untuk spam.")
                return
            text_spam = message.text.split(None, 4)[4]

        dspam_processes[message.chat.id] = {
            "count_message": count_message,
            "count_delay": count_delay,
            "text_spam": text_spam,
            "is_cancelled": False,
        }

        if delay_until_start > 0:
            scheduled_time_str = scheduled_dt.strftime("%H:%M")
            await msg.edit(f"Pesan akan dikirim pada {scheduled_time_str} WIB.")
            await asyncio.sleep(delay_until_start)

        for i in range(count_message):
            if dspam_processes[message.chat.id]["is_cancelled"]:
                break
            if reply:
                await reply.copy(message.chat.id)
            else:
                await message.reply(text_spam, quote=False)
            await asyncio.sleep(count_delay)

    except ValueError as e:
        await msg.edit(
            f"Kesalahan dalam memasukkan jumlah pesan, penundaan, atau waktu: {str(e)}"
        )
    except Exception as error:
        await msg.edit(str(error))
    finally:
        dspam_processes.pop(message.chat.id, None)
        with suppress(Exception):
            await msg.delete()
            await message.delete()


async def list_dspam(client, message):
    if not dspam_processes:
        await message.reply("Tidak ada proses dspam yang sedang berjalan.")
        return

    text = "Proses dspam sedang berjalan di grup ini:\n"
    index = 1
    for chat_id, process_info in dspam_processes.items():
        try:
            chat = await client.get_chat(chat_id)
            chat_name = chat.title
            now = datetime.now(pytz.timezone("Asia/Jakarta"))
            finish_time = now + timedelta(
                seconds=process_info["count_message"] * process_info["count_delay"]
            )

            text += f"{index}. {chat_name} (Selesai pada: {finish_time.strftime('%H:%M%S')} WIB, Penundaan: {process_info['count_delay']} detik, Kata-kata: {process_info['text_spam']})\n"
            index += 1
        except Exception as e:
            text += f"- {chat_id} (Gagal mendapatkan nama grup: {str(e)})\n"
    await message.reply(text)


async def cancel_dspam(client, message):
    if message.chat.id not in dspam_processes:
        await message.reply("Tidak ada proses dspam yang sedang berjalan di grup ini.")
        return

    if len(message.command) == 1:
        dspam_processes[message.chat.id]["is_cancelled"] = True
        await message.reply("Proses dspam berhasil dibatalkan.")
    else:
        try:
            if message.command[1].lower() == "all":
                for chat_id, process_info in dspam_processes.items():
                    process_info["is_cancelled"] = True
                await message.reply("Semua proses dspam berhasil dibatalkan.")
            else:
                cancel_index = int(message.command[1])
                if cancel_index <= 0 or cancel_index > len(dspam_processes):
                    await message.reply("Nomor proses dspam tidak valid.")
                    return

                chat_id_to_cancel = list(dspam_processes.keys())[cancel_index - 1]
                dspam_processes[chat_id_to_cancel]["is_cancelled"] = True
                await message.reply(
                    f"Proses dspam nomor {cancel_index} berhasil dibatalkan."
                )
                dspam_processes.pop(chat_id_to_cancel)
        except ValueError:
            await message.reply("Silakan masukkan nomor proses dspam yang valid.")


async def addtext_cmd(client, message):
    if len(message.command) < 2:
        await message.reply("Silakan berikan kata-kata yang ingin ditambahkan.")
        return

    new_text = " ".join(message.command[1:])
    if message.chat.id in dspam_processes:
        dspam_processes[message.chat.id]["text_spam"] += f" {new_text}"
        await message.reply(
            f"Kata-kata '{new_text}' berhasil ditambahkan ke dalam proses dspam."
        )
    else:
        await message.reply("Tidak ada proses dspam yang sedang berjalan di grup ini.")
