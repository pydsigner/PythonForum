from PythonForum import app
from PythonForum.database.forum import Forum
from flask import render_template

@app.route("/")
def index():
    categories = Forum.objects.first().categories
    return render_template("index.html", categories=categories)
