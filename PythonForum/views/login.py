from couchdb.mapping import Document

class DbUser(Document):
    pass


class User(object):
    def __init__(self, email, username):
        self.email = email
        self.username = username

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

def load_user(data):
    return User(data['email'], "SOME USER")

def return_user_by_id(user_id):
    pass