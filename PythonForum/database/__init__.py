from couchdb import Server

try:
    from dev_config import server
except ImportError:
    server = ""

server = Server(server)
