import json
from os import read

defaults = {
    "running": True,
    "session": "lin"
}

storagePath = "/tmp/whatsAuto.data"

with open(storagePath, 'w') as f:
    json.dump(defaults, f, indent=2)




def readData():
    with open(storagePath, "r") as a_file:
        json_object = json.load(a_file)
        return json_object
json_object = readData()

def updateData(key, value):
    json_object[key]=value
    with open(storagePath, 'w') as a_file:
        json.dump(json_object, a_file)
    
    return

#updateData(key="running", value=False)

print(readData()['session'])