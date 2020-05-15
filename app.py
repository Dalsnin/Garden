from flask import Flask, render_template

app = Flask(__name__)

hello = 2 + 5

@app.route("/")
def index():
    return render_template("index.html")