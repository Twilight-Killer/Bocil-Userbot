from PyroUbot import *

__MODULE__ = "spam"
__HELP__ = """
<b>『 bantuan tagall』</b>

  <b>• perintah:</b> <code>{0}tagall</code> [typemessage/reply message ] 
  <b>• penjelasan:</b> ngetag semua anggota group

  <b>• perintah:</b> <code>{0}batal</code>
  <b>• penjelasan:</b> mematikan ngetag

  <b>• perintah:</b> <code>{0}spam</code> [jumlah_pesan - pesan_spam]
  <b>• penjelasan:</b> untuk spam

  <b>• perintah:</b> <code>{0}dspam</code> [jumlah_pesan - jumlah_delay_detik - pesan_spam]
  <b>• penjelasan:</b> untuk spam pesan delay

  <b>• perintah:</b> <code>{0}spmlist</code> 
  <b>• penjelasan:</b> melihat list dspam

  <b>• perintah:</b> <code>{0}henti</code>
  <b>• penjelasan:</b> menghentikan dspam

  <b>• perinta:</b> <code>{0}ddtext</code>
  <b>• penjelasan:</b> menambahkan text dspam
"""


@PY.UBOT("tagall")
async def _(client, message):
    await tagall_cmd(client, message)


@PY.UBOT("batal")
async def _(client, message):
    await batal_cmd(client, message)


@PY.UBOT("spam")
async def _(client, message):
    await spam_cmd(client, message)


@PY.UBOT("dspam")
async def _(client, message):
    await dspam_cmd(client, message)


@PY.UBOT("spmlist")
async def _(client, message):
    await list_dspam(client, message)


@PY.UBOT("henti")
async def _(client, message):
    await cancel_dspam(client, message)


@PY.UBOT("ddtext")
async def _(client, message):
    await addtext_cmd (client, message)
