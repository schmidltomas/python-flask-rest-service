from sqlalchemy.exc import IntegrityError
from src.exceptions import ResourceExists, ResourceNotFound
from src.model import Dataset, DatasetDwhType
from src.schema import DatasetSchema


class DatasetRepository:

	@staticmethod
	def create(schema: DatasetSchema) -> dict:
		try:
			dataset = Dataset(schema.get('name'), schema.get('type'), schema.get('title'))
			dataset.save()

			ref = schema.get('ref')
			dataset_dwh_type = DatasetDwhType(
				ref.get('type'), ref.get('subtype'), ref.get('table'), ref.get('primaryKey'),
				ref.get('properties'), dataset.id)
			dataset_dwh_type.save()

			created_dataset = Dataset.find_by_name(schema.get('name'))
			return DatasetSchema().dump(created_dataset)
		except IntegrityError:
			Dataset.rollback()
			raise ResourceExists('Dataset name=' + schema.get('name') + ' already exists.')

	@staticmethod
	def get_by_name(name: str) -> dict:
		dataset = Dataset.find_by_name(name)

		if dataset is None:
			raise ResourceNotFound('Dataset name=' + name + ' not found.')
		else:
			return DatasetSchema().dump(dataset)

	@staticmethod
	def get_by_id(id: str) -> dict:
		dataset = Dataset.find_by_id(id)

		if dataset is None:
			raise ResourceNotFound('Dataset id=' + id + ' not found.')
		else:
			return DatasetSchema().dump(dataset)

	@staticmethod
	def get_all() -> dict:
		datasets = Dataset.find_all()
		return DatasetSchema().dump(datasets, many=True)

	@staticmethod
	def put(id: str, schema: DatasetSchema) -> dict:
		updated_dataset = Dataset.find_by_id(id)

		if updated_dataset is None:
			raise ResourceNotFound('Dataset id=' + id + ' not found.')
		else:
			updated_dataset.update(schema)
			updated_dataset.ref.update(schema.get('ref'))
			return DatasetSchema().dump(updated_dataset)

	@staticmethod
	def delete(id: str):
		dataset = Dataset.find_by_id(id)

		if dataset is None:
			raise ResourceNotFound('Dataset id=' + id + ' not found.')
		else:
			dataset.delete()
