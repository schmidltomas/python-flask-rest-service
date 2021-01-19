from flask import request, jsonify
from flask_restful import Resource, reqparse
from src.repository import DatasetRepository
from ..exceptions import ResourceException


class Dataset(Resource):
	@staticmethod
	def get(id: str):
		try:
			dataset = DatasetRepository.get_by_id(id)
			return dataset, 200
		except ResourceException as ex:
			return ex.to_dict()

	@staticmethod
	def put(id: str):
		try:
			dataset = DatasetRepository.put(id)
			return dataset, 200
		except ResourceException as ex:
			return ex.to_dict()

	@staticmethod
	def delete(id: str):
		try:
			DatasetRepository.delete(id)
			return '', 204
		except ResourceException as ex:
			return ex.to_dict()


class DatasetList(Resource):
	@staticmethod
	def post():
		request_json = request.get_json(silent=True)
		name: str = request_json['name']
		object_type: str = request_json['type']
		title: str = request_json.get('title', '')
		ref: dict = request_json.get('ref', '')

		try:
			dataset = DatasetRepository.create(name, object_type, title, ref)
			return dataset, 200
		except ResourceException as ex:
			return ex.to_dict()

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
			return ex.to_dict()
