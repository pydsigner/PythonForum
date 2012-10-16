from PythonForum import app
from flask import render_template

@app.route("/forum/<int:forum_id>/")
def category(forum_id):
    return render_template("category.html")
