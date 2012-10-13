from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.browserid import BrowserID
import time

from views.login import load_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '7\xae\xfa\x0c\xad\x07~\xfb\x9f=\x19\xec\xc0\x0f;8\xeb\xe1\x12\xc0\xee\x042\x89n\n\xfb\xcd\xf1\x04\xda\x87'


login_manager = LoginManager()
login_manager.user_loader(lambda x: x)
login_manager.init_app(app)

browser_id = BrowserID()
browser_id.user_loader(load_user)
browser_id.init_app(app)

@app.route("/servertime")
def time_at_server():
    return time.asctime()

@app.route("/")
def index():
    return render_template("index.html")