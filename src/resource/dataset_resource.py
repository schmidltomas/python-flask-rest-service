from flask import request, jsonify
from flask_restful import Resource, reqparse
from src.repository import DatasetRepository
from src.schema import DatasetSchema
from ..exceptions import ResourceException
from src.schema import Validator

validator = Validator('./src/schema/json/dataset.schema.json')


class Dataset(Resource):
	@staticmethod
	def get(id: str):
		try:
			dataset = DatasetRepository.get_by_id(id)
			return dataset, 200
		except ResourceException as ex:
			return ex.to_dict(), ex.status_code

	@staticmethod
	def put(id: str):
		try:
			# TODO to method
			request_json = request.get_json(silent=True)
			validator.validate(request_json)
			schema = DatasetSchema().load(request_json)
			dataset = DatasetRepository.put(id, schema)
			return dataset, 200
		except ResourceException as ex:
			return ex.to_dict(), ex.status_code

	@staticmethod
	def delete(id: str):
		try:
			DatasetRepository.delete(id)
			return '', 204
		except ResourceException as ex:
			return ex.to_dict(), ex.status_code


class DatasetList(Resource):
	@staticmethod
	def post():
		try:
			# TODO to method
			request_json = request.get_json(silent=True)
			validator.validate(request_json)
			schema = DatasetSchema().load(request_json)
			dataset = DatasetRepository.create(schema)
			return dataset, 200
		except ResourceException as ex:
			return ex.to_dict(), ex.status_code

	@staticmethod
	def get():
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, required=False)
		args = parser.parse_args()

		try:
			if args['name'] is not None:
				dataset = DatasetRepository.get_by_name(args['name'])
				return dataset, 200
			else:
				datasets = DatasetRepository.get_all()
				return datasets, 200
		except ResourceException as ex:
			return ex.to_dict(), ex.status_code
