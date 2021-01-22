# python-flask-rest-service
Exercise project - backend service with REST API in Python &amp; Flask.

# Run in Docker
From root directory, run:
```
docker-compose up
```

# Run locally
Setup virtual environment:
```
python3 -m venv venv
virtualenv venv
source venv/bin/activate
```

Install dependencies:
```
pip install flask
pip install python-dotenv
pip install psycopg2
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-marshmallow
pip install flask-restful
pip install marshmallow
pip install marshmallow-sqlalchemy
pip install jsonschema
pip install exrex
```

Create the database:
```
psql -U postgres -c "CREATE DATABASE apgqi1djut1d5f9u_md;"
flask db init
flask db migrate
flask db upgrade
```

And run Flask app:
```
flask run
```
