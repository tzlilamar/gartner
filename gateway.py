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
        mqttc.username_pw_set(os.environ.get("MQTT_USER", ''), os.environ.get("MQTT_PWD", ''))
        mqttc.connect(os.environ.get("MQTT_HOST", ''), int(os.environ.get("MQTT_PORT", 	5001)))
        mqttc.publish('fb-posts-updates',json.dumps(
                    int(content['entry'][0]['time']),'LIKE',
                    content['entry'][0]['changes'][0]['value']['sender_id']))
        mqttc.disconnect()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',	5000)))