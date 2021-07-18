from flask import Flask, request, render_template
from flask_cors import CORS
from random import random
from hashlib import md5
import json






import json

from werkzeug.utils import redirect

defaults = {
    "session": "logged In",
    "status": "running"
}

jsonObject =  json.loads(json.dumps(defaults))


def updateData(key, value):
    jsonObject[key]==value
    return

def createKey():
    return md5((str(random()).encode())).hexdigest()


app = Flask(__name__)

#secretKey = createKey()
#print(f"SECRET KEY: {secretKey}")

# FOr cors

CORS(app)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method=='GET':
        return "<h1 style='color:red;'>FUCK YOU!</h1>"
    elif request.method=='POST':
        return "^FLAG{GO_FUCK_YOUR_SELF}^"


@app.route("/controller")
def controller():
    session = jsonObject['session']
    status = jsonObject['status']
    return render_template('controller.html', session=session, status=status)


@app.route("/api/update/key=<key>&value=<value>")
def update(key, value):
    updateData(key, value)
    return redirect('/controller')



@app.route('/api/data/')
def apiData():
    return jsonObject



@app.route('/api/login', methods=["POST"])
def api():
    keyInp = request.headers.get('secret')
    if keyInp == None:
        return 401

    #elif keyInp==secretKey:
    #    return "Authorized successfully"
    else:

        return 401



app.debug=True
app.run(host='127.0.0.1', port=6464, threaded=True)