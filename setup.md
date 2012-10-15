# Set up

## Install dependencies

Install [MongoDb]

Install [mongoengine]

Install [flask]

Install [flask-login]

Install [flask-browserid]

Add the file `db_config.py` in PythonForum directory with the line
    db_uri = mongodb://<Server Name>

Run `$ mongod --dbpath <path-to-db>`

Add PythonForum to PYTHONPATH and run `python -m PythonForum`

[MongoDb]: http://www.mongodb.org/display/DOCS/Quickstart
[mongoengine]: http://mongoengine.org/#getting-started
[flask]: http://flask.pocoo.org/
[flask-login]: https://github.com/maxcountryman/flask-login#installation
[flask-browserid]: https://github.com/garbados/flask-browserid#installation
