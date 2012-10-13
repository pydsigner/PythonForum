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
        self.authd = True

    def is_authenticated(self):
        return self.authd

    def is_active(self):
        return self.active

    def is_anonymous(self):
        """I am not a number I am a man!"""
        return False

    def get_id(self):
        return self.id


def get_user_by_id(userid):
    """Return an Avatar for the given userid."""
    user = User.load(user_database, userid)
    return Avatar(user.id, user.email, user.username, user.active)

def get_user(data):
    """Return or create a user from data handed to us by BrowserID(Persona)"""
    if data['status'] == "okay":
        # get user or create
        email = data['email']
        result = User.by_email(user_database, key=email)
        try:
            current_user = result.rows[0]
        except IndexError:
            print "user doesn't exist."
            # User doesn't exist. Create user now
            current_user = User(email=email, username=email, active=True)
            current_user.store(user_database)
        return Avatar(current_user.id, current_user.email, current_user.username, current_user.active)
    else:
        return None # Failed to auth with persona