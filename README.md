# python-flask-rest-service
Exercise project - backend service with REST API in Python &amp; Flask.

# Run in Docker
From root directory, run:
```
docker-compose up
```

# Run locally
Setup virtual environment and install Python requirements:
```
python3 -m venv venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create and migrate the database:
```
psql -U postgres -c "CREATE DATABASE apgqi1djut1d5f9u_md;"
flask db init
flask db migrate
flask db upgrade
```

Run Flask app:
```
flask run
```

# REST API
The service runs on `localhost:5000` and exposes a simple REST API:
```
POST /datasets
GET /datasets/<id>
GET /datasets?name=<name>
GET /datasets
PUT /datasets/<id>
DELETE /datasets/<id>
```

An example of a dataset can be found in `/test/json/clients.json`

# Tests
Run unit test from the root folder:
```
python3 -m unittest test.test_rest
```

Note: it may be required to set env variables from `/.flaskenv` manually to run the test with separate `python` command.
