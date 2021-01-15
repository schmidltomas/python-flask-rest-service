from sqlalchemy.exc import IntegrityError
from src.exceptions import ResourceExists
from src.model import Dataset, DatasetDwhType
from src.schema import DatasetSchema


class DatasetRepository:

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

	# TODO reuse method?
	@staticmethod
	def get(name: str) -> dict:
		dataset = Dataset.query.filter_by(name=name).first_or_404()
		dataset = DatasetSchema().dump(dataset)
		return dataset
