import json
from pprint import pprint

with open('strings.json') as data_file:    
    data = json.load(data_file)
pprint(data["usuarios_mensuales"][10]["usuarios"])
print(len(data["usuarios_mensuales"]))
