from motor.motor_asyncio import AsyncIOMotorClient
from PyroUbot.config import MONGO_URL

ubotdb = mongodb.ubot

async def get_user_data():
    """
    Get user data from the database.
    """
    data = []
    async for ubot in ubotdb.find({"user_id": {"$exists": 1}}):
        data.append({
            "name": str(ubot["user_id"]),
            "api_id": ubot["api_id"],
            "api_hash": ubot["api_hash"],
            "session_string": ubot["session_string"]
        })
    return data

async def add_ubot(user_id, api_id, api_hash, session_string):
    """
    Add a userbot to the database.
    """
    await ubotdb.update_one(
        {"user_id": user_id},
        {"$set": {"api_id": api_id, "api_hash": api_hash, "session_string": session_string}},
        upsert=True,
    )

async def remove_ubot(user_id):
    """
    Remove a userbot from the database.
    """
    await ubotdb.delete_one({"user_id": user_id})

async def get_userbots():
    """
    Get all userbots from the database.
    """
    data = []
    async for ubot in ubotdb.find({"user_id": {"$exists": 1}}):
        data.append(
            {
                "name": str(ubot["user_id"]),
                "api_id": ubot["api_id"],
                "api_hash": ubot["api_hash"],
                "session_string": ubot["session_string"],
            }
        )
    return data
