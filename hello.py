from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/other")
def other():
    return render_template("other.html")


@app.route("/click")
def click():
    print("clicked on div")
    return render_template("clicked.html")

