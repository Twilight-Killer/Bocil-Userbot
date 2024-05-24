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
        msg_afk = (
            f"<b>❏ sedang afk\n ╰ alasan: {self.reason}</b>"
            if self.reason
            else "<b>❏ sedang afk</b>"
        )
        await set_vars(self.client.me.id, "AFK", db_afk)
        await self.message.reply(msg_afk)

    async def get_afk(self):
        vars = await get_vars(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_reason = vars.get("reason")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = (
                f"<b>❏ sedang afk\n ├ waktu: {afk_runtime}\n ╰ alasan: {afk_reason}</b>"
                if afk_reason
                else f"<b>❏ sedang afk\n ╰ waktu: {afk_runtime}</b>"
            )
            return await self.message.reply(afk_text)

    async def unset_afk(self):
        vars = await get_vars(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = f"<b>❏ kembali online\n ╰ afk selama: {afk_runtime}"
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
