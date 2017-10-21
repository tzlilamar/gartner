#!flask/bin/python
from flask import Flask
import paho.mqtt.client as mqtt
import os
from flask import request

mqttc = mqtt.Client()
app = Flask(__name__)
url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')


@app.route('/')
def getRequest():
    return "Hello World!"

@app.route('/webhook', methods=['POST'])
def postRequest():
    return "post works"

@app.route('/webhook', methods=['GET'])
def getToPostRequest():
    request.args.get ("hub.challenge")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))