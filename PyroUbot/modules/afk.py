from time import time

from PyroUbot import *

__MODULE__ = "afk"
__HELP__ = """
<b>『 bantuan afk 』</b>

  <b>• perinta:</b> <code>{0}afk</code></code>
  <b>• penjelasan:</b> mengaktifkan afk

  <b>• perintah:</b> <code>{0}unafk</code></code>
  <b>• penjelasan:</b> menonaktifkan afk
"""

class AFK:
    def __init__(self, client, message, reason=""):
        self.client = client
        self.message = message
        self.reason = reason

    async def set_afk(self):
        db_afk = {"time": time(), "reason": self.reason}
        if self.client.me.is_premium:
            msg_afk = (
                f"<emoji id=5971865795582495562>🔺</emoji> <b>Sedang AFK\n<emoji id=6226230182806554486>🚫</emoji> Alasan: {self.reason}</b>"
                if self.reason
                else "<emoji id=5971865795582495562>🔺</emoji> <b>Sedang AFK</b>"
            )
        else:
            msg_afk = f"<b>❏ Sedang AFK\n ╰ Alasan: {self.reason}</b>" if self.reason else "<b>❏ Sedang AFK</b>"
        
        await set_vars(self.client.me.id, "AFK", db_afk)
        await self.message.reply(msg_afk)

    async def get_afk(self):
        vars = await get_vars(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_reason = vars.get("reason")
            afk_runtime = await get_time(time() - afk_time)
            if self.client.me.is_premium:
                afk_text = (
                    f"<emoji id=4927486932113425461>🔺</emoji> <b>Sedang AFK\n<emoji id=5413704112220949842>✅</emoji> Waktu: {afk_runtime}\n<emoji id=5305417940760273444>🚫</emoji> Alasan: {afk_reason}</b>"
                    if afk_reason
                    else f"<emoji id=4927486932113425461>🔺</emoji> <b>Sedang AFK\n<emoji id=5413704112220949842>✅</emoji> Waktu: {afk_runtime}</b>"
                )
            else:
                afk_text = (
                    f"<b>❏ Sedang AFK\n ├ Waktu: {afk_runtime}\n ╰ Alasan: {afk_reason}</b>"
                    if afk_reason
                    else f"<b>❏ Sedang AFK\n ╰ Waktu: {afk_runtime}</b>"
                )
            return await self.message.reply(afk_text)

    async def unset_afk(self):
        vars = await get_vars(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_runtime = await get_time(time() - afk_time)
            if self.client.me.is_premium:
                afk_text = f"<emoji id=5190744409901113661>🌐</emoji> <b>Kembali online\n<emoji id=5413704112220949842>✅</emoji> AFK selama: {afk_runtime}</b>"
            else:
                afk_text = f"<b>❏ Kembali online\n ╰ AFK selama: {afk_runtime}</b>"
            await self.message.reply(afk_text)
            return await remove_vars(self.client.me.id, "AFK")

@PY.UBOT("afk")
async def _(client, message):
    reason = get_arg(message)
    afk_handler = AFK(client, message, reason)
    await afk_handler.set_afk()

@PY.AFK()
async def _(client, message):
    afk_handler = AFK(client, message)
    await afk_handler.get_afk()

@PY.UBOT("unafk")
async def _(client, message):
    afk_handler = AFK(client, message)
    return await afk_handler.unset_afk()
