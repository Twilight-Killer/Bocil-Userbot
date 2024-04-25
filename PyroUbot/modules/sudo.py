from .. import *

__MODULE__ = "sudo"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴜᴅᴏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addsudo</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> tambah addsudo

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delsudo</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> hapus addsudo
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}getsudo</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> cek list sudo
"""


@PY.UBOT("addsudo")
async def addsudo(client, message):
    msg = await message.edit_text("<b>Sedang memproses...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit_text(
            "<b>Harap balas ke user atau ketik user_id yang ingin ditambahkan ke daftar sudo</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit_text(str(error))

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if user.id in sudo_users:
        return await msg.edit_text(
            f"<b>✨ {user.first_name} {user.last_name or ''} sudah berada dalam daftar sudo</b>"
        )

    try:
        await add_to_vars(client.me.id, "SUDO_USERS", user.id)
        return await msg.edit_text(
            f"<b>✅ {user.first_name} {user.last_name or ''} berhasil ditambahkan ke daftar sudo</b>"
        )
    except Exception as error:
        return await msg.edit_text(str(error))


@PY.UBOT("delsudo")
async def delsudo(client, message):
    msg = await message.edit_text("<b>Sedang memproses...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit_text(
            "<b>Harap balas ke user atau ketik user_id yang ingin dihapus dari daftar sudo</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit_text(str(error))

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if user.id not in sudo_users:
        return await message.reply(
            f"<b>✨ {user.first_name} {user.last_name or ''} tidak ada dalam daftar sudo</b>"
        )

    try:
        await remove_from_vars(client.me.id, "SUDO_USERS", user.id)
        return await msg.edit_text(
            f"<b>❌ {user.first_name} {user.last_name or ''} berhasil dihapus dari daftar sudo</b>"
        )
    except Exception as error:
        return await msg.edit_text(str(error))


@PY.UBOT("getsudo")
async def getsudo(client, message):
    msg = await message.edit_text("<b>Sedang memproses...</b>")
    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if not sudo_users:
        return await msg.edit_text("<s>Daftar sudo kosong</s>")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await client.get_users(int(user_id))
            sudo_list.append(
                f" ├ {user.first_name} {user.last_name or ''} | <code>{user.id}</code>"
            )
        except:
            continue

    if sudo_list:
        response = (
            "<b>❏ Daftar sudo:</b>\n"
            + "\n".join(sudo_list)
            + f"\n <b>╰ Total sudo_users:</b> <code>{len(sudo_list)}</code>"
        )
        return await msg.edit_text(response)
    else:
        return await msg.edit_text("<b>Tidak dapat mengambil daftar sudo saat ini</b>")
