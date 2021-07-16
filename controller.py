from os import system
from subprocess import Popen as run
import json


def getData():
	with open('/tmp/whatsAuto/controller.json', 'r') as f:
		data = json.load(f)
	return data

def runController():

	data = {"session":"loggedIn"}
	with open('/tmp/whatsAuto/controller.json', 'w') as f:
	    json.dump(data, f)
	    print("Logged In")

	run([
		'xterm',
		'-T',
		'Whatsapp Controller',
		'-e',
		'python3',
		'/tmp/whatsAuto/controller.py',
		'&&',
		'sleep',
		'10'
		])
	return



def createAndRun():
	system('rm -rf /tmp/whatsAuto; mkdir /tmp/whatsAuto')
	controller = """

import json

print("Whatsapp controller...")

def getData():
    with open('/tmp/whatsAuto/controller.json', 'r') as f:
        data = json.load(f)
    return data


while True:
    command = input(">> ")

    if 'logout' in command.lower():
        data = {"session":"loggedOut"}
        with open('/tmp/whatsAuto/controller.json', 'w') as f:
            json.dump(data, f)
            print("Logged out")

    elif 'status' in command.lower():
        status = getData()['session']
        print(status)

    elif 'exit' in command.lower():
        exit("🚫 Bye")
        break

    else:
        print("Not a command")


	"""

	with open('/tmp/whatsAuto/controller.py', 'w') as f:
		f.write(controller)

	runController()
