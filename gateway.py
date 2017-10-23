#!flask/bin/python
from flask import Flask
from flask import request
import paho.mqtt.client as mqtt
import os
from flask import json

mqttc = mqtt.Client()
app = Flask(__name__)
url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')


@app.route("/")
def getRequest():
    return "Hello World!"


@app.route('/webhook', methods=['GET'])
def getToPostRequest():
    return request.args.get("hub.challenge")


@app.route("/webhook", methods=['POST'])
def postRequestTofb():
    content = request.get_json()
    if content['entry'][0]['changes'][0]['value']['item'] == 'like':
        mqttc.publish('fb-posts-updates',json.dumps(
                    int(content['entry'][0]['time']),'LIKE',
                    content['entry'][0]['changes'][0]['value']['sender_id']))


if __name__ == '__main__':
    app.run(host='m10.cloudmqtt.com', port=int(os.environ.get('PORT', 17954)))