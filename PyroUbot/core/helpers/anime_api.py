import random

import requests
from pyrogram.enums import MessagesFilter


class API:
    def wall(client):
        anime_channel = random.choice(["@animehikarixa", "@Anime_WallpapersHD"])
        animenya = []
        async for anime in client.search_messages(
            anime_channel, filter=MessagesFilter.PHOTO
        ):
            animenya.append(anime)
        return random.choice(animenya)

    def nsfw():
        url = "https://www.waifu.im/search/?included_tags=hentai"
        response = requests.get(url)
        content = response.text
        start_index = content.find("var files = [") + len("var files = ")
        end_index = content.find("]", start_index)
        files_str = content[start_index:end_index]
        files = [file.strip('" ') for file in files_str.split(",")]
        return random.choice(files)
