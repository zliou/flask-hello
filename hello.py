from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><a href='/there'>let's go</a>"



@app.route("/there")
def hello_there():
    return "<p>hello there!</p>"
