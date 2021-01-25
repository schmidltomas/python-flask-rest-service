# python-flask-rest-service
Exercise project - backend service with REST API in Python &amp; Flask.

# Run in Docker
From root directory, run:
```
docker-compose up
```

# Run locally
Setup virtual environment and install Python dependencies:
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
