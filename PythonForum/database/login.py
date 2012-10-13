from couchdb.mapping import *
import couchdb
from PythonForum.database import server

try:
    user_database = server.create("pf-userdb")
except couchdb.PreconditionFailed:
    user_database = server["pf-userdb"]

class User(Document):
    email = TextField()
    username = TextField()
    active = BooleanField()

    by_email = ViewField("searches", """
    function(doc) {
        emit(doc.email, doc);
    }
    """)

class Avatar(object):
    def __init__(self, id, email, username, active):
        self.id = id
        self.username = username
        self.active = active
        self.email = email

    def is_active(self):
        return self.active

    def is_anonymous(self):
        """I am not a number I am a man!"""
        return False

    def get_id(self):
        return self.id

def get_user_by_id(userid):
    """Return an Avatar for the given userid."""
    return User.load(user_database, userid)

def get_user(data):
    """Return or create a user from data handed to us by BrowserID(Persona)"""
    if data['status'] == "okay":
        # get user or create
        email = data['email']
        rows = User.by_email(user_database, key=email)
        try:
            user = rows[0]
        except IndexError:
            # User doesn't exist. Create user now
            user = User(email=email, username=email, active=True)
            user.store(user_database)
        return Avatar(user.id, user.email, user.username, user.active)
    else:
        return None # Failed to auth with persona