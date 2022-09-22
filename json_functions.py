import json
from pprint import pprint as pp

def write_json(file_path:str, data):
    f = open(file_path, 'w')
    # pp(data)
    js_str = json.dumps(data, indent=4)
    #print(js_str)
    f.write(js_str)
    f.close()

def read_json(file_path:str):
    f = open(file_path, 'r')
    js_str = f.read()
    #print(js_str)
    data = json.loads(js_str)
    #pp(data)
    f.close()
    return data
