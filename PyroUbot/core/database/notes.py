from PyroUbot.core.database import mongo_client

collection = mongo_client["PyroUbot"]["notes"]

async def save_note(user_id, note_name, message):
    doc = {"_id": user_id, "notes": {note_name: message}}
    try:
        result = await collection.find_one({"_id": user_id})
        if result:
            await collection.update_one(
                {"_id": user_id}, {"$set": {f"notes.{note_name}": message}}
            )
        else:
            await collection.insert_one(doc)
    except:
        return False
    return True

async def get_note(user_id, note_name):
    result = await collection.find_one({"_id": user_id})
    if result is not None:
        try:
            note_id = result["notes"][note_name]
            return note_id
        except KeyError:
            return None
    return None

async def rm_note(user_id, note_name):
    try:
        await collection.update_one(
            {"_id": user_id}, {"$unset": {f"notes.{note_name}": ""}}
        )
        return True
    except:
        return False

async def all_notes(user_id):
    try:
        results = await collection.find_one({"_id": user_id})
        notes_dic = results.get("notes", {})
        key_list = notes_dic.keys()
        return key_list
    except:
        return None

async def rm_all(user_id):
    try:
        await collection.update_one({"_id": user_id}, {"$unset": {"notes": ""}})
        return True
    except:
        return False
