from PyroUbot.core.database import mongodb

chatsdb = mongodb.chats

async def get_chat(user_id):
    chat = await chatsdb.find_one({"chat": user_id})
    if not chat:
        return []
    return chat.get("list", [])

async def add_chat(user_id, chat_id):
    chat_list = await get_chat(user_id)
    if chat_id not in chat_list:
        chat_list.append(chat_id)
        try:
            await chatsdb.update_one({"chat": user_id}, {"$set": {"list": chat_list}}, upsert=True)
            return True
        except:
            return False
    return False

async def remove_chat(user_id, chat_id):
    chat_list = await get_chat(user_id)
    if chat_id in chat_list:
        chat_list.remove(chat_id)
        try:
            await chatsdb.update_one({"chat": user_id}, {"$set": {"list": chat_list}}, upsert=True)
            return True
        except:
            return False
    return False
