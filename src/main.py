from flask import Flask, jsonify, request
from flask_restful import Api
from flask_migrate import Migrate
from src.resources import Dataset, DatasetList
from src.models import Dataset as DatasetModel, db
# from app.model.dataset import Dataset, DatasetSchema
# from app.model.md_object_type import MdObjectType
from .app import create_app

app = create_app()
migrate = Migrate(app, db)

api = Api(app)
api.add_resource(DatasetList, '/datasets')
api.add_resource(Dataset, '/datasets/<name>')

