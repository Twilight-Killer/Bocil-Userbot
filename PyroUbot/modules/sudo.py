from PyroUbot import *

__MODULE__ = "sudo"
__HELP__ = """
<b>『 bantuan sudo』</b>

  <b>• perintah:</b> <code>{0}addsudo</code>
  <b>• penjelasan:</b> tambah addsudo

  <b>• perintah:</b> <code>{0}delsudo</code>
  <b>• penjelasan:</b> hapus addsudo
  
  <b>• perintah:</b> <code>{0}getsudo</code>
  <b>• penjelasan:</b> cek list sudo
"""

@PY.UBOT("addsudo")
async def addsudo(client, message):
    if message.from_user.id != client.me.id:
        msg = await message.reply("<b>Sedang memproses...</b>")
    else:
        msg = await message.edit_text("<b>Sedang memproses...</b>")

    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit_text(
            "<b>Harap balas ke user atau ketik user_id yang ingin ditambahkan ke daftar sudo</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit_text(f"<b>Error:</b> {str(error)}")

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
        return await msg.edit_text(f"<b>Error:</b> {str(error)}")


@PY.UBOT("delsudo")
async def delsudo(client, message):
    if message.from_user.id != client.me.id:
        msg = await message.reply("<b>Sedang memproses...</b>")
    else:
        msg = await message.edit_text("<b>Sedang memproses...</b>")

    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit_text(
            "<b>Harap balas ke user atau ketik user_id yang ingin dihapus dari daftar sudo</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit_text(f"<b>Error:</b> {str(error)}")

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if user.id not in sudo_users:
        return await msg.edit_text(
            f"<b>✨ {user.first_name} {user.last_name or ''} tidak ada dalam daftar sudo</b>"
        )

    try:
        await remove_from_vars(client.me.id, "SUDO_USERS", user.id)
        return await msg.edit_text(
            f"<b>❌ {user.first_name} {user.last_name or ''} berhasil dihapus dari daftar sudo</b>"
        )
    except Exception as error:
        return await msg.edit_text(f"<b>Error:</b> {str(error)}")


@PY.UBOT("getsudo")
async def getsudo(client, message):
    if message.from_user.id != client.me.id:
        msg = await message.reply("<b>Sedang memproses...</b>")
    else:
        msg = await message.edit_text("<b>Sedang memproses...</b>")

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if not sudo_users:
        return await msg.edit_text("<b>Daftar sudo kosong</b>")

    sudo_list = []
    batch_size = 50
    for i in range(0, len(sudo_users), batch_size):
        batch = sudo_users[i:i + batch_size]
        for user_id in batch:
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
            + f"\n<b>╰ Total sudo_users:</b> <code>{len(sudo_list)}</code>"
        )
        return await msg.edit_text(response)
    else:
        return await msg.edit_text("<b>Tidak dapat mengambil daftar sudo saat ini</b>")
