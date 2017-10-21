#!flask/bin/python
from flask import Flask
import paho.mqtt.client as mqtt
import os

mqttc = mqtt.Client()
app = Flask(__name__)
url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')


@app.route('/')
def getRequest():
    return "Hello World!"

@app.route('/webhook', methods=['POST'])
def postRequest():
    return "post works"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))