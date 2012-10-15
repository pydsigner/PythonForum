# Set up

## Install dependencies

Install [MongoDb]
Install [mongoengine]
Install [flask]
Install [flask-login]
Install [flask-browserid]

get mongo server set up
add db_config.py with the line "db_uri = mongodb://<Server Name>"
run "$ mongod --dbpath <path-to-db>"
Add PythonForum to PYTHONPATH and run "python -m PythonForum"

[MongoDb]: http://www.mongodb.org/display/DOCS/Quickstart
[mongoengine]: http://mongoengine.org/#getting-started
[flask]: http://flask.pocoo.org/
[flask-login]: https://github.com/maxcountryman/flask-login#installation
[flask-browserid]: https://github.com/garbados/flask-browserid#installation
