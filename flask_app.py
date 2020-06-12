# $env:FLASK_APP = "flask_app.py"

from flask import Flask, render_template

from databases import get_blogposts

app = Flask(__name__)


@app.route("/")
def index():
    blogentries = get_blogposts.get_blogposts()
    metadata = dict(
        listlen = len(blogentries)
    )
    return render_template("index.html", blogentries=blogentries, metadata=metadata)

@app.route("/overview.html")
def overview():
    blogentries = get_blogposts.get_blogposts()
    metadata = dict(
        listlen = len(blogentries)
    )
    return render_template("overview.html", blogentries=blogentries, metadata=metadata)

@app.route("/pictures.html")
def pictures():
    return render_template("pictures.html")

@app.route("/about.html")
def about():
    return render_template("about.html")