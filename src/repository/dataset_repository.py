from sqlalchemy.exc import IntegrityError
from src.exceptions import ResourceExists
from src.model import Dataset, DatasetDwhType
from src.schema import DatasetSchema
from flask import request


class DatasetRepository:

	# TODO also use request object?
	@staticmethod
	def create(name: str, title: str, ref: dict) -> dict:
		try:
			dataset = Dataset(name, "dataset", title)
			dataset.save()

			dataset_dwh_type = DatasetDwhType(
				ref.get('type'), ref.get('subtype'), ref.get('table'), ref.get('primaryKey'),
				ref.get('properties'), dataset.id)
			dataset_dwh_type.save()

			saved_dataset = Dataset.query.filter_by(name=dataset.name).first_or_404()
			result = DatasetSchema().dump(saved_dataset)
		except IntegrityError:
			Dataset.rollback()
			raise ResourceExists('Dataset name=' + name + ' already exists.')

		return result

	@staticmethod
	def get(name: str) -> dict:
		dataset = Dataset.query.filter_by(name=name).first_or_404()
		dataset = DatasetSchema().dump(dataset)
		return dataset

	@staticmethod
	def get_all() -> dict:
		datasets = Dataset.query.all()
		datasets = DatasetSchema().dump(datasets, many=True)
		return datasets

	@staticmethod
	def put(name: str) -> dict:
		# TODO
		return {}

	@staticmethod
	def delete(name: str):
		dataset = Dataset.query.filter_by(name=name).first_or_404()
		dataset.delete()
