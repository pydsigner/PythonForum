from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.browserid import BrowserID
import time

from database.login import get_user, get_user_by_id

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xad\xdb\xe9o\x84\x03S\xa93\xc2X\x0ejlq\xad\xcd1\xb0Ub'

login_manager = LoginManager()
login_manager.user_loader(get_user_by_id)
login_manager.init_app(app)

browser_id = BrowserID()
browser_id.user_loader(get_user)
browser_id.init_app(app)

@app.route("/servertime")
def time_at_server():
    return time.asctime()

@app.route("/")
def index():
    return render_template("index.html")