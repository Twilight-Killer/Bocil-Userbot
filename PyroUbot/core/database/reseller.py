from PyroUbot import logger
from PyroUbot.core.database import mongodb

resell = mongodb.seles


async def get_seles():
    try:
        seles = await resell.find_one({"seles": "seles"})
        if not seles:
            return []
        return seles.get("reseller", [])
    except Exception as e:
        logger.error(f"Error while getting resellers: {e}")
        return []


async def add_seles(user_id):
    try:
        reseller = await get_seles()
        reseller.append(user_id)
        await resell.update_one(
            {"seles": "seles"}, {"$set": {"reseller": reseller}}, upsert=True
        )
        return True
    except Exception as e:
        logger.error(f"Error while adding reseller: {e}")
        return False


async def remove_seles(user_id):
    try:
        reseller = await get_seles()
        if user_id in reseller:
            reseller.remove(user_id)
            await resell.update_one(
                {"seles": "seles"}, {"$set": {"reseller": reseller}}, upsert=True
            )
        return True
    except Exception as e:
        logger.error(f"Error while removing reseller: {e}")
        return False
