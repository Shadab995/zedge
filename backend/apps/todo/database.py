import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

users_collection = database.get_collection("users_collection")


# helpers


def users_helper(users) -> dict:
    return {
        "id": str(users["_id"]),
        "username": users["username"],
        "password": users["password"],
    }