import asyncio
from random import randint

from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputPeerChannel, InputPeerChat

from PyroUbot import *

__MODULE__ = "vctools"
__HELP__ = """
<b>『 bantuan vctools 』</b>

  <b>• perintah:</b> <code>{0}startvc</code>
  <b>• penjelasan:</b> mulai os gc
  
  <b>• perintah:</b> <code>{0}joinvc</code>
  <b>• penjelasan:</b> join os gc

  <b>• perintah:</b> <code>{0}stopvc</code>
  <b>• penjelasan:</b> stop os gc
  
  <b>• perintah:</b> <code>{0}leavevc</code>
  <b>• penjelasan:</b> turun os gc
  """

list_data = []

def remove_list(user_id):
    global list_data
    list_data = [item for item in list_data if item.get("id") != user_id]

def add_list(client, chat_id):
    async def add_list_async(client, chat_id):
        try:
            chat = await client.get_chat(chat_id)
            user_id = client.me.id
            # Check if the user already exists in the list
            if not any(item.get("id") == user_id for item in list_data):
                data = {
                    "id": user_id,
                    "nama": f"• <b>[{client.me.first_name} {client.me.last_name or ''}](tg://user?id={user_id})</b> di <code>{chat.title}</code>",
                }
                list_data.append(data)
        except Exception as e:
            print(f"Error in add_list_async: {e}")

    asyncio.create_task(add_list_async(client, chat_id))

def get_list():
    if not list_data:
        return "Tidak ada pengguna dalam obrolan suara saat ini."
    return "\n".join(item["nama"] for item in list_data)

async def get_group_call(client, message):
    try:
        chat_peer = await client.resolve_peer(message.chat.id)
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.invoke(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
        else:
            full_chat = None

        if full_chat and hasattr(full_chat, 'call') and full_chat.call:
            return full_chat.call

        await message.reply("Tidak ada obrolan suara aktif.")
    except Exception as e:
        await message.reply(f"Error in get_group_call: {e}")
    return None

@PY.UBOT("startvc")
async def _(client, message):
    flags = " ".join(message.command[1:])
    msg = await message.reply("<code>Memproses...</code>")
    vctitle = message.text.split(None, 1)[1] if len(message.command) > 1 else None
    chat_id = message.chat.id if message.chat else None

    if not chat_id:
        await msg.edit("<b>INFO:</b> Tidak dapat menentukan chat ID.")
        return

    args = f"<b>Obrolan suara aktif</b>\n<b>Chat: </b><code>{message.chat.title}</code>"

    try:
        if vctitle:
            args += f"\n<b>Title: </b> <code>{vctitle}</code>"

        await asyncio.sleep(1) 
        await client.invoke(
            CreateGroupCall(
                peer=(await client.resolve_peer(chat_id)),
                random_id=randint(10000, 999999999),
                title=vctitle if vctitle else None,
            )
        )
        await msg.edit(args)
    except pyrogram.errors.FloodWait as e:
        await asyncio.sleep(e.value) 
        await msg.edit(f"<b>INFO:</b> FloodWait of {e.value} seconds.")
    except Exception as e:
        await msg.edit(f"<b>INFO:</b> `{e}`")

@PY.UBOT("stopvc")
async def _(client, message):
    msg = await message.reply("<code>Memproses...</code>")
    group_call = await get_group_call(client, message)

    if not group_call:
        return

    try:
        await asyncio.sleep(1) 
        await client.invoke(DiscardGroupCall(call=group_call))
        await msg.edit(
            f"<b>Obrolan suara diakhiri</b>\n<b>Chat: </b><code>{message.chat.title}</code>"
        )
    except pyrogram.errors.FloodWait as e:
        await asyncio.sleep(e.value) 
        await msg.edit(f"<b>INFO:</b> FloodWait of {e.value} seconds.")
    except Exception as e:
        await msg.edit(f"<b>INFO:</b> `{e}`")

@PY.UBOT("joinvc")
async def _(client, message):
    msg = await message.reply("<b>Tunggu sebentar...</b>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    chat_title = message.chat.title if hasattr(message.chat, 'title') else 'Obrolan'

    try:
        await asyncio.sleep(1) 
        await client.group_call.start(chat_id, join_as=client.me.id)
        await msg.edit(f"<b>Berhasil bergabung ke obrolan suara</b>\n<b>Group: </b><code>{chat_title}</code>")
        await asyncio.sleep(5)
        await client.group_call.set_is_mute(True)
        add_list(client, chat_id)
    except pyrogram.errors.FloodWait as e:
        await asyncio.sleep(e.value) 
        await msg.edit(f"<b>INFO:</b> FloodWait of {e.value} seconds.")
    except Exception as e:
        await msg.edit(f"ERROR: {e}")

@PY.UBOT("leavevc")
async def _(client, message):
    msg = await message.reply("<b>Tunggu sebentar...</b>")
    chat_title = message.chat.title if hasattr(message.chat, 'title') else 'Obrolan'

    try:
        await asyncio.sleep(1) 
        await client.group_call.stop()
        remove_list(client.me.id)
        await msg.edit(f"<b>Berhasil turun dari obrolan suara</b>\n<b>Group: </b><code>{chat_title}</code>")
    except pyrogram.errors.FloodWait as e:
        await asyncio.sleep(e.value)  
        await msg.edit(f"<b>INFO:</b> FloodWait of {e.value} seconds.")
    except Exception as e:
        await msg.edit(f"ERROR: {e}")

@PY.UBOT("listvc", FILTERS.OWNER)
async def _(client, message):
    chat_title = message.chat.title if hasattr(message.chat, 'title') else 'Obrolan'
    voice_chat_list = get_list()
    await message.reply(f"<b>Daftar Pengguna dalam Obrolan Suara {chat_title}:</b>\n\n{voice_chat_list}")
