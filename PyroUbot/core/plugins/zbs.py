from pyrogram.enums import ChatMemberStatus

from PyroUbot import*


async def zombies_cmd(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    
    member = await client.get_chat_member(chat_id, user_id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await message.reply("Anda harus menjadi admin atau pemilik grup untuk menggunakan perintah ini.")
    
    deleted_users = []
    banned_users = 0
    Tm = await message.reply("Sedang memeriksa...")
    
    async for i in client.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    
    if len(deleted_users) > 0:
        for deleted_user in deleted_users:
            try:
                banned_users += 1
                await message.chat.ban_member(deleted_user)
            except Exception:
                pass
        await Tm.edit(f"Berhasil mengeluarkan {banned_users} akun terhapus")
    else:
        await Tm.edit("Tidak ada akun terhapus di grup ini")
