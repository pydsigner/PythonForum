from PythonForum.database import users_db
from PythonForum import app
from mongoengine import *

class User(Document):
    email = StringField(required=True)
    username = StringField()
    active = BooleanField()

class Avatar(object):
    def __init__(self, email, username, active):
        self.username = username
        self.active = active
        self.email = email
        self.authd = True

    def is_authenticated(self):
        return self.authd

    def is_active(self):
        return self.active

    def is_anonymous(self):
        """I am not a number I am a man!"""
        return False

    def get_id(self):
        return self.email

def get_user_by_id(userid):
    """Return an Avatar for the given userid."""
    user = User.objects(email=userid).first()
    return Avatar(user.email, user.username, user.active)

def get_user(data):
    """Return or create a user from data handed to us by BrowserID(Persona)"""
    if data['status'] == "okay":
        # get user or create
        email = data['email']
        current_user = User.objects(email=email).first()
        print current_user
        if current_user is None:
            # User doesn't exist. Create user now
            current_user = User(email=email, username=email, active=True)
            current_user.save()
        return Avatar(current_user.email, current_user.username, current_user.active)
    else:
        return None # Failed to auth with persona