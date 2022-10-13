from aiohttp import ClientSession
from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

async def queryGH(query: str, variables: dict = {}) -> dict:
    json = {
        'query': query,
        'variables': variables
    }

    headers = {
        'Authorization': f'Bearer {getenv("GHTOKEN")}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    async with ClientSession() as session:
        async with session.post('https://api.github.com/graphql', json=json, headers=headers) as response:
            json = await response.json()

            return json['data']
