from motor.motor_asyncio import AsyncIOMotorClient
from PyroUbot.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.pyro_ubot

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

# Menggunakan async def untuk fungsi-fungsi yang melakukan operasi yang membutuhkan waktu
async def add_ubot(user_id, api_id, api_hash, session_string):
    await ubotdb.update_one(
        {"user_id": user_id},
        {"$set": {"api_id": api_id, "api_hash": api_hash, "session_string": session_string}},
        upsert=True,
    )

# Menggunakan async def untuk fungsi-fungsi yang melakukan operasi yang membutuhkan waktu
async def remove_ubot(user_id):
    await ubotdb.delete_one({"user_id": user_id})

# Menggunakan async def untuk fungsi-fungsi yang melakukan operasi yang membutuhkan waktu
async def get_userbots():
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
