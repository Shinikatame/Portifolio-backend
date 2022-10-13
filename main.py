from fastapi import FastAPI
from uvicorn import run

from importlib import import_module
from os import listdir

app = FastAPI()

def load(path = 'Routers'): 
    for file in listdir(path):
        if file not in ['__pycache__', '__init__.py']:
            if file.endswith('.py'):
                module = import_module(f'{path}.{file}'.replace('.py', ''))
                app.include_router(module.router)

            else:
                load(path + '/' + file)

load()

if __name__ == '__main__': 
    run(app)