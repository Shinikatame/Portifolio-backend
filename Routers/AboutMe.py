from fastapi import APIRouter

from Modules.QueryGH import queryGH
from Modules.ReadFile import reader

router = APIRouter()

@router.get('/aboutme')
async def aboutme():
    about = await queryGH(reader('GraphQL/User.txt'))
    return about['user']
