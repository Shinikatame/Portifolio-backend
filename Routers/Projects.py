from fastapi import APIRouter
from asyncio import create_task, gather

from Modules.QueryGH import queryGH
from Modules.ReadFile import reader

from Database.Repos import findRepos

router = APIRouter()

@router.get('/projects')
async def projects():
    sampleRepos = await findRepos()
    reposData = []

    for repo in sampleRepos:
        query = reader('GraphQL/Repo.txt')
        variables = {'name': repo}

        task = create_task(queryGH(query, variables))
        reposData.append(task)

    await gather(*reposData)

    return [repo.result()['repository'] for repo in reposData]
