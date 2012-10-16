# Set up

## Install dependencies

Run `pip install -r requirements.txt`

or install each dependency.

Install [MongoDb]

Install [mongoengine]

Install [flask]

Install [flask-login]

Install [flask-browserid]

## Server setup

Add the file `db_config.py` in PythonForum directory with the line
`db_uri = 'mongodb://<Server Name>'`

Add PythonForum to PYTHONPATH

## Running the Forum

Run `$ mongod --dbpath PythonForum/database/`

Run `$ python -m PythonForum`

Navigate to wherever you named the server, and enjoy.

[MongoDb]: http://www.mongodb.org/display/DOCS/Quickstart
[mongoengine]: http://mongoengine.org/#getting-started
[flask]: http://flask.pocoo.org/
[flask-login]: https://github.com/maxcountryman/flask-login#installation
[flask-browserid]: https://github.com/garbados/flask-browserid#installation
