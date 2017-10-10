#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def getRequest():
    return "Hello World!"

@app.route('/', methods=['POST'])
def postRequest():
    return "post works"



if __name__ == '__main__':
    app.run(debug=True)