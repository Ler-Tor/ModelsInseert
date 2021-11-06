import requests as re
import json


def insertData(filename, arType, port, insertType):
    json_file = open(filename, "r")
    data = json.load(json_file)
    for item in data[arType]:
        if insertType == "post":
            r = re.post(f"http://167.99.212.13:{port}/{arType}", data = json.dumps(item))
            print(r.text)
        else:
            r = re.put(f"http://167.99.212.13:{port}/{arType}/{item['id']}", data = json.dumps(item))
            print(r.text) 


if __name__ == '__main__':
    insertData("category.json", "arcategory", 18084, "pu")
    insertData("models.json", "armodels", 18084, "pu")
    
