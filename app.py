from flask import Flask, request, abort
from pymongo import MongoClient
from bson.json util import dumps, default 

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(port=8000, debug=True)