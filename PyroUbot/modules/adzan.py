import requests

from PyroUbot import *

__MODULE__ = "adzan"
__HELP__ = """
<b>『 bantuan adzan』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}adzan</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> jadwal adzan sesuai kota
"""

@PY.UBOT("adzan")
async def adzan_command(client, message):
    if len(message.command) < 2:
        return await message.reply("<b>Silahkan Masukkan Nama Kota Anda</b>")
    
    LOKASI = message.text.split(None, 1)[1]
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    try:
        request = requests.get(url)
        request.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
    except requests.exceptions.HTTPError as err:
        return await message.reply(f"<b>Maaf Tidak Menemukan Kota <code>{LOKASI}</code></b>")
    
    result = request.json()
    catresult = f"""
Jadwal Shalat Hari Ini

<b>Tanggal</b> <code>{result['items'][0]['date_for']}</code>
<b>Kota</b> <code>{result['query']} | {result['country']}</code>

<b>Terbit:</b> <code>{result['items'][0]['shurooq']}</code>
<b>Subuh:</b> <code>{result['items'][0]['fajr']}</code>
<b>Zuhur:</b> <code>{result['items'][0]['dhuhr']}</code>
<b>Ashar:</b> <code>{result['items'][0]['asr']}</code>
<b>Maghrib:</b> <code>{result['items'][0]['maghrib']}</code>
<b>Isya:</b> <code>{result['items'][0]['isha']}</code>
"""
    await message.reply(catresult)
