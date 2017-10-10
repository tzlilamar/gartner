#!flask/bin/python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def getRequest():
    return "Hello World!"

@app.route('/', methods=['POST'])
def postRequest():
    return "post works"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))