# python-flask-rest-service
Exercise project - backend service with REST API in Python &amp; Flask.

# Setup
1. python3 -m venv venv
2. virtualenv venv
3. source venv/bin/activate
4. pip install flask
5. pip install python-dotenv
6. pip install marshmallow
7. pip install flask-sqlalchemy
8. pip install flask-migrate
9. pip install psycopg2
9. pip install flask-restful
9. pip install exrex

# DB migration
1. psql -U postgres -c "CREATE DATABASE apgqi1djut1d5f9u_md;"
2. flask db init
3. flask db migrate -m "dataset table"
4. flask db upgrade
