import json
import requests

creds = {
    "Content-Type": "application/json",
}

data = {
    "unning": False,
    
}



r = requests.put('http://localhost:5000/api/update', headers=creds, json=data)


print(r.text)