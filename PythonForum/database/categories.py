from mongoengine import *

from threads import Thread

class Category(Document):
    """
    A category object represents a list of topics.
    """
    topics = ListField(ReferenceField(Thread, dbref=False))
    name = StringField()
    description = StringField()