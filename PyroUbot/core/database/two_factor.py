from PyroUbot.core.database import mongo_client

factor_collection = mongo_client["PyroUbot"].get_collection("factor")


async def get_two_factor(user_id):
    user = await factor_collection.find_one({"_id": user_id})
    if user:
        return user.get("expire_date")
    else:
        return None

async def set_two_factor(user_id, expire_date):
    await factor_collection.update_one(
        {"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True
    )

async def rem_two_factor(user_id):
    await factor_collection.update_one(
        {"_id": user_id}, {"$unset": {"expire_date": ""}}, upsert=True
    )
