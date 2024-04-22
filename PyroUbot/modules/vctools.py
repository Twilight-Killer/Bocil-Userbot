import asyncio
from random import randint

from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputPeerChannel, InputPeerChat

from PyroUbot import *

__MODULE__ = "vctools"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟꜱ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}startvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}joinvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stopvc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋʜɪʀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}leavevc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ
  """


list_data = []

def remove_list(user_id):
    list_data[:] = [item for item in list_data if item.get("id") != user_id]


def add_list(client, chat_id):
    async def add_list_async(client, chat_id):
        chat = await client.get_chat(chat_id)
        data = {
            "id": client.me.id,
            "nama": f"• <b>[{client.me.first_name} {client.me.last_name or ''}](tg://user?id={client.me.id})</b> di <code>{chat.title}</code>",
        }
        list_data.append(data)

    asyncio.create_task(add_list_async(client, chat_id))

def get_list():
    if not list_data:
        return "Tidak ada pengguna dalam obrolan suara saat ini."

    return "\n".join(item["nama"] for item in list_data)


async def get_group_call(client, message):
    chat_peer = await client.resolve_peer(message.chat.id)

    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat

        if full_chat is not None:
            return full_chat.call

    await message.reply("ɴᴏ ɢʀᴏᴜᴘ ᴄᴀʟʟ ꜰᴏᴜɴᴅ")
    return False


@PY.UBOT("startvc")
async def _(client, message):
    flags = " ".join(message.command[1:])
    msg = await message.reply("<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</code>")
    vctitle = get_arg(message)
    chat_id = message.chat.title if flags == ChatType.CHANNEL else message.chat.id

    args = f"<b>ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴀᴋᴛɪꜰ</b>\n<b>ᴄʜᴀᴛ : </b><code>{chat_id}</code>"

    try:
        if vctitle:
            args += f"\n<b>ᴛɪᴛʟᴇ : </b> <code>{vctitle}</code>"

        await client.invoke(
            CreateGroupCall(
                peer=(await client.resolve_peer(chat_id)),
                random_id=randint(10000, 999999999),
                title=vctitle if vctitle else None,
            )
        )
        await msg.edit(args)
    except Exception as e:
        await msg.edit(f"<b>INFO:</b> `{e}`")


@PY.UBOT("stopvc")
async def _(client, message):
    msg = await message.reply("<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</code>")
    group_call = await get_group_call(client, message)

    if not group_call:
        return

    await client.invoke(DiscardGroupCall(call=group_call))
    await msg.edit(
        f"<b>ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴅɪᴀᴋʜɪʀɪ</b>\n<b>ᴄʜᴀᴛ : </b><code>{message.chat.title}</code>"
    )


@PY.UBOT("joinvc")
async def _(client, message):
    msg = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ....</b>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    chat_title = message.chat.title
    try:
        await client.group_call.start(chat_id, join_as=client.me.id)
    except Exception as e:
        return await msg.edit(f"ERROR: {e}")
    await msg.edit(f"<b>ʙᴇʀʜᴀsɪʟ ɴᴀɪᴋ ᴋᴇ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ</b>\n<b>ɢʀᴏᴜᴘ : </b><code>{chat_title}</code>")
    await asyncio.sleep(5)
    await client.group_call.set_is_mute(True)
    add_list(client, chat_id)


@PY.UBOT("leavevc")
async def _(client, message):
    msg = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ....</b>")
    chat_title = message.chat.title
    try:
        await client.group_call.stop()
    except Exception as e:
        return await msg.edit(f"ERROR: {e}")
    remove_list(client.me.id)
    return await msg.edit(f"<b>ʙᴇʀʜᴀsɪʟ ᴛᴜʀᴜɴ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ</b>\n<b>ɢʀᴏᴜᴘ : </b><code>{chat_title}</code>")

@PY.UBOT("listvc")
async def _(client, message):
    chat_title = message.chat.title
    voice_chat_list = get_list()
    await message.reply(f"<b>Daftar Pengguna dalam Obrolan Suara {chat_title}:</b>\n\n{voice_chat_list}")
