from pyrogram import filters
from pyrogram.types import Message
from database import get_var, set_var


from PyroUbot import *

# Command: !pmwlcm {on/off}
@PY.UBOT("pmwlcm")
async def pmwlcm(client, message):
    status = message.command[1].lower()
    if status in ["on", "off"]:
        set_var("pmwlcm_status", status)
        await message.reply(f"Pesan sambutan telah di{'hidupkan' if status == 'on' else 'matikan'}")
    else:
        await message.reply("Gunakan 'on' atau 'off' untuk mengaktifkan atau menonaktifkan pesan sambutan")

# Command: !setpmwlcm {text/reply}
@PY.UBOT("setpmwlcm")
async def setpmwlcm(client, message):
    set_var("pmwlcm_text", message.text.split(maxsplit=1)[1])
    await message.reply("Pesan sambutan telah disetel")

# Command: !pmfilter {on/off}
@PY.UBOT("pmfilter")
async def pmfilter(client, message):
    status = message.command[1].lower()
    if status in ["on", "off"]:
        set_var("pmfilter_status", status)
        await message.reply(f"Filter chat pribadi telah di{'hidupkan' if status == 'on' else 'matikan'}")
    else:
        await message.reply("Gunakan 'on' atau 'off' untuk mengaktifkan atau menonaktifkan filter chat pribadi")

# Command: !addpmfilter {filter_name} {text/reply}
@PY.UBOT("addpmfilter")
async def addpmfilter(client, message):
    parts = message.text.split(maxsplit=2)
    if len(parts) == 3:
        set_var(f"pmfilter_{parts[1]}", parts[2])
        await message.reply(f"Filter {parts[1]} telah ditambahkan")
    else:
        await message.reply("Gunakan format: !addpmfilter {filter_name} {text/reply}")

# Command: !delpmfilter {filter_name}
@PY.UBOT("delpmfilter")
async def delpmfilter(client, message):
    filter_name = message.command[1]
    if get_var(f"pmfilter_{filter_name}"):
        set_var(f"pmfilter_{filter_name}", "")
        await message.reply(f"Filter {filter_name} telah dihapus")
    else:
        await message.reply(f"Filter {filter_name} tidak ditemukan")

# Command: !delallpmfilter
@PY.UBOT("delallpmfilter")
async def delallpmfilter(client, message):
    for var_name in get_var():
        if var_name.startswith("pmfilter_"):
            set_var(var_name, "")
    await message.reply("Semua filter chat pribadi telah dihapus")

# Command: !listpmfilter
@PY.UBOT("listpmfilter")
async def listpmfilter(client, message):
    filters_list = [var_name.replace("pmfilter_", "") for var_name in get_var() if var_name.startswith("pmfilter_")]
    if filters_list:
        await message.reply("Daftar filter chat pribadi: \n" + "\n".join(filters_list))
    else:
        await message.reply("Belum ada filter chat pribadi yang tersimpan")
