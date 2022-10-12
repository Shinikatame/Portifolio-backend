from motor.motor_asyncio import AsyncIOMotorClient

from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

client = AsyncIOMotorClient(getenv('DATABASE'))
db = client.get_database('main')

mongo = db.portfolio

async def findRepos():
    return await mongo.find_one({'_id' : 'repositories'})