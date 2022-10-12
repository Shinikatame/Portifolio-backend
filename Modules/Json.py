from json import load

def jsonLoad(path: str):
    with open(path, 'r+', encoding = 'UTF-8') as file:
        return load(file)