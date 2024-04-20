from PyroUbot.core.database import mongodb

user = mongodb.premium

async def get_prem():
    prem = await user.find_one({"prem": "prem"})
    if not prem:
        return []
    return prem.get("list", [])

async def add_prem(user_id):
    try:
        list_ = await get_prem()
        list_.append(user_id)
        await user.update_one({"prem": "prem"}, {"$set": {"list": list_}}, upsert=True)
        return True
    except:
        return False

async def remove_prem(user_id):
    try:
        list_ = await get_prem()
        if user_id in list_:
            list_.remove(user_id)
            await user.update_one({"prem": "prem"}, {"$set": {"list": list_}}, upsert=True)
            return True
        return False
    except:
        return False
