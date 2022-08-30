from flask import Flask
from stability_sdk import client

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"