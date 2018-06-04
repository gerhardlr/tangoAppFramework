from flask import Flask
from flask import request
from PyTango import DeviceProxy
import time

app = Flask(__name__)

def init():
    pass


def close():
    pass

@app.route("/")
def hello():
    return "test works"


@app.route("/api/")
def api():
    return "in api"


@app.route('/api/<domain>/<deviceClass>/<deviceInstance>/')
def getDevice(domain,deviceClass,deviceInstance):
    dev = DeviceProxy(domain+"/"+deviceClass+"/"+deviceInstance)
    return domain+"/"+deviceClass+"/"+deviceInstance

@app.route('/api/<domain>/<deviceClass>/<deviceInstance>/', methods=['POST'])
def cmdDevice(domain,deviceClass,deviceInstance):
    dev = DeviceProxy(domain+"/"+deviceClass+"/"+deviceInstance)
    json_data = request.get_json()
    cmd_name = json_data["cmd_name"]
    cmd_param = json_data["cmd_param"]
    if (cmd_param== "None"):
        result = dev.command_inout(cmd_name)
    else:
        result = dev.command_inout(cmd_name,cmd_param)
    return cmd_name