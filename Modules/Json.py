from json import load, dump
    
def jsonCreater(data: list | tuple | dict, path: str = 'test.json'):
    with open(path, 'w+', encoding = 'UTF-8') as file:
        dump(data, file, indent = 4)  

def jsonLoad(path: str = 'test.json'):
    with open(path, 'r+', encoding = 'UTF-8') as file:
        return load(file)