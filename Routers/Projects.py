from fastapi import APIRouter
from asyncio import create_task, gather

from Modules.QueryGH import queryGH
from Modules.ReadFile import reader

from Database.Repos import findRepos

router = APIRouter()

@router.get('/projects')
async def projects():
    sampleRepos = await findRepos()
    reposTask = []

    for repo in sampleRepos['repositories']:
        query = reader('GraphQL/Repo.txt')
        variables = {'name': repo}

        task = create_task(queryGH(query, variables))
        reposTask.append(task)

    await gather(*reposTask)

    reposData = [repo.result()['repository'] for repo in reposTask]

    return reposData
