from flask import Flask, jsonify, request
from flask_restful import Api
from flask_migrate import Migrate
from src.resource import Dataset, DatasetList
from src.model import db
from flask_migrate import Migrate
from .app import create_app

app = create_app()
migrate = Migrate(app, db)

api = Api(app)
api.add_resource(DatasetList, '/datasets')
api.add_resource(Dataset, '/datasets/<name>')


# TODO:
#  - int database enums
#  - exception handling
#  - input validation
#  - pagination
#  - tests
#  - docstrings
