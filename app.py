from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Well this is the start of something interesting eh"

