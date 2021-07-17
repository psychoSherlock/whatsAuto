from flask import Flask, request
from random import random
from hashlib import md5
import json


def createKey():
    return md5((str(random()).encode())).hexdigest()


app = Flask(__name__)

secretKey = createKey()
print(f"SECRET KEY: {secretKey}")



dickt = {
    "running": True
}

jsDump = json.dumps(dickt)
jsData = json.loads(jsDump)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method=='GET':
        return "<h1 style='color:red;'>FUCK YOU!</h1>"
    elif request.method=='POST':
        return "^FLAG{GO_FUCK_YOUR_SELF}^"


@app.route('/api/login', methods=["POST"])
def api():
    keyInp = request.headers.get('secret')
    if keyInp == None:
        return "Unauthorized"
    elif keyInp==secretKey:
        return "Authorized successfully"
    else:

        return "Unauthorized"
@app.route('/api/update', methods=["POST", "PUT"])
def apiUpdate():
    running = jsData['running'] if request.json['running'] else request.json
    #data = request.json
    jsData['running'] = str(running)
    return jsData




if __name__=='__main__':
    app.debug=True
    app.run(host='127.0.0.1')