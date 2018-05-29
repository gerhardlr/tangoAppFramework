from flask import Flask
from flask import request
from PyTango import DeviceProxy
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "test works"

@app.route("/api/")
def api():
	return "in api"
@app.route('/api/<domain>/<deviceClass>/<deviceInstance>/',methods=['POST'])
def getDevice(domain,deviceClass,deviceInstance):
	dev = DeviceProxy(domain+"/"+deviceClass+"/"+deviceInstance)
	command = request.args.get('command','')ß
		dev.command_inout(command)
	return "in getDevice, command = "+command



if __name__ == '__main__':
    app.run(host='0.0.0.0')
 
 ##FLASK_APP=app.py flask run