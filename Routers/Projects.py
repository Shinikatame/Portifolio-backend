from fastapi import APIRouter
from asyncio import create_task, gather

from Modules.QueryGH import queryGH
from Modules.ReadFile import reader

from Database.Repos import findRepos

router = APIRouter()

async def queryRepo(query: str, repoName: str):
    variables = {'name': repoName}

    repoRequest = await queryGH(query, variables)
    repo = repoRequest['repository']

    repo['languages'] = [lang['name'] for lang in repo['languages']['nodes']]
    repo['primaryLanguage'] = repo['primaryLanguage']['name']

    return repo

@router.get('/projects')
async def projects():
    sampleRepos = await findRepos()
    queryGraphql = reader('GraphQL/Repos.txt')
    reposTask = []

    for repoName in sampleRepos['repositories']:
        task = create_task(queryRepo(queryGraphql, repoName))
        reposTask.append(task)

    await gather(*reposTask)

    reposData = [repo.result() for repo in reposTask]

    return reposData
