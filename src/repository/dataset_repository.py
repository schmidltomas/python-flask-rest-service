from sqlalchemy.exc import IntegrityError
from src.exceptions import ResourceExists
from src.model import Dataset, DatasetDwhType
from src.schema import DatasetSchema
from flask import request
import json


class DatasetRepository:

	# TODO use Dataset object as method param?
	@staticmethod
	def create(name: str, object_type: str, title: str, ref: dict) -> dict:
		try:
			dataset = Dataset(name, object_type, title)
			dataset.save()

			dataset_dwh_type = DatasetDwhType(
				ref.get('type'), ref.get('subtype'), ref.get('table'), ref.get('primaryKey'),
				ref.get('properties'), dataset.id)
			dataset_dwh_type.save()

			created_dataset = Dataset.find_by_name(name)
			return DatasetSchema().dump(created_dataset)
		except IntegrityError:
			Dataset.rollback()
			raise ResourceExists('Dataset name=' + name + ' already exists.')

	@staticmethod
	def get(name: str) -> dict:
		dataset = Dataset.find_by_name(name)
		return DatasetSchema().dump(dataset)

	@staticmethod
	def get_all() -> dict:
		datasets = Dataset.find_all()
		return DatasetSchema().dump(datasets, many=True)

	@staticmethod
	def put(name: str) -> dict:
		request_dict = json.loads(request.data)
		updated_dataset = Dataset.find_by_name(name)
		updated_dataset.update(**request_dict)
		updated_dataset.ref.update(**request_dict.get('ref'))
		return DatasetSchema().dump(updated_dataset)

	@staticmethod
	def delete(name: str):
		dataset = Dataset.find_by_name(name)
		dataset.delete()
