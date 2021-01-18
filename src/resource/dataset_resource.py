from flask import request, jsonify
from flask_restful import Resource

from src.repository import DatasetRepository


class Dataset(Resource):
	@staticmethod
	def get(name: str):
		dataset = DatasetRepository.get(name)
		return dataset, 200

	@staticmethod
	def put(name: str):
		dataset = DatasetRepository.put(name)
		return dataset, 200

	@staticmethod
	def delete(name: str):
		DatasetRepository.delete(name)
		return '', 204


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
		except Exception as ex:
			print(ex)
			# response = jsonify(ex)
			# response.status_code = ex.status_code
			# return response
			return None

	@staticmethod
	def get():
		datasets = DatasetRepository.get_all()
		return datasets, 200
