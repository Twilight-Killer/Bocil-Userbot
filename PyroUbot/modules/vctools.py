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
  <b>• penjelasan:</b> mulai obrolan suara di grup (OS GC)
  
  <b>• perintah:</b> <code>{0}joinvc</code>
  <b>• penjelasan:</b> bergabung ke obrolan suara di grup
  
  <b>• perintah:</b> <code>{0}stopvc</code>
  <b>• penjelasan:</b> mengakhiri obrolan suara di grup
  
  <b>• perintah:</b> <code>{0}leavevc</code>
  <b>• penjelasan:</b> keluar dari obrolan suara di grup
  
  <b>• perintah:</b> <code>{0}listvc</code>
  <b>• penjelasan:</b> daftar pengguna dalam obrolan suara
"""


voice_chat_participants = {}
MAX_PARTICIPANTS = 100

async def add_participant(client, chat_id):
    try:
        user = await client.get_me()
        chat = await client.get_chat(chat_id)
        
        if chat_id not in voice_chat_participants:
            voice_chat_participants[chat_id] = {}

        if user.id not in voice_chat_participants[chat_id]:
            user_data = f"[{user.first_name}](tg://user?id={user.id})"
            chat_title = chat.title
            voice_chat_participants[chat_id][user.id] = {"user": user_data, "chat": chat_title}
    except Exception as e:
        logger.error(f"Error in add_participant: {e}")

def remove_participant(chat_id, user_id):
    if chat_id in voice_chat_participants and user_id in voice_chat_participants[chat_id]:
        voice_chat_participants[chat_id].pop(user_id, None)

def get_participants_list(chat_id):
    if chat_id not in voice_chat_participants or not voice_chat_participants[chat_id]:
        return "Tidak ada pengguna dalam obrolan suara saat ini."

    participants = "\n".join(
        f"• {data['user']} di grup <code>{data['chat']}</code>"
        for data in voice_chat_participants[chat_id].values()
    )
    total_participants = len(voice_chat_participants[chat_id])
    return f"{participants}\n\n<b>Total pengguna:</b> {total_participants}"

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
async def start_vc(client, message):
    msg = await message.reply("<code>Memproses...</code>")
    vctitle = message.text.split(None, 1)[1] if len(message.command) > 1 else None
    chat_id = message.chat.id if message.chat else None

    if not chat_id:
        await msg.edit("<b>INFO:</b> Tidak dapat menentukan chat ID.")
        return

    args = f"<b>Obrolan suara aktif</b>\n<b>Grup: </b><code>{message.chat.title}</code>"

    try:
        if vctitle:
            args += f"\n<b>Judul: </b><code>{vctitle}</code>"

        await client.invoke(
            CreateGroupCall(
                peer=(await client.resolve_peer(chat_id)),
                random_id=randint(10000, 999999999),
                title=vctitle
            )
        )
        await msg.edit(args)
    except Exception as e:
        await msg.edit(f"<b>INFO:</b> {e}")

@PY.UBOT("stopvc")
async def stop_vc(client, message):
    msg = await message.reply("<code>Memproses...</code>")
    group_call = await get_group_call(client, message)

    if not group_call:
        await msg.edit("Tidak ada obrolan suara aktif yang ditemukan.")
        return

    try:
        await client.invoke(DiscardGroupCall(call=group_call))
        await msg.edit(
            f"<b>Obrolan suara diakhiri</b>\n<b>Grup: </b><code>{message.chat.title}</code>"
        )
        # Kosongkan daftar peserta untuk obrolan ini
        if message.chat.id in voice_chat_participants:
            del voice_chat_participants[message.chat.id]
    except Exception as e:
        await msg.edit(f"<b>INFO:</b> {e}")

@PY.UBOT("joinvc")
async def join_vc(client, message):
    msg = await message.reply("<b>Tunggu sebentar...</b>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    chat_title = message.chat.title if hasattr(message.chat, 'title') else 'Obrolan'

    try:
        await client.group_call.start(chat_id)
        await msg.edit(f"<b>Berhasil bergabung ke obrolan suara</b>\n<b>Grup: </b><code>{chat_title}</code>")
        await asyncio.sleep(5)
        await client.group_call.set_is_mute(True)
        await add_participant(client, chat_id)
    except Exception as e:
        await msg.edit(f"ERROR: {e}")

@PY.UBOT("leavevc")
async def leave_vc(client, message):
    msg = await message.reply("<b>Tunggu sebentar...</b>")
    chat_id = message.chat.id
    chat_title = message.chat.title if hasattr(message.chat, 'title') else 'Obrolan'

    try:
        await client.group_call.stop()
        remove_participant(chat_id, client.me.id)
        await msg.edit(f"<b>Berhasil keluar dari obrolan suara</b>\n<b>Grup: </b><code>{chat_title}</code>")
    except Exception as e:
        await msg.edit(f"ERROR: {e}")

@PY.UBOT("listvc", FILTERS.OWNER)
async def list_vc(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title if hasattr(message.chat, 'title') else 'Obrolan'
    voice_chat_list = get_participants_list(chat_id)
    await message.reply(f"<b>Daftar Pengguna dalam Obrolan Suara:</b>\n\n{voice_chat_list}")
