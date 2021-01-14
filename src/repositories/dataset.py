from sqlalchemy.exc import IntegrityError
from src.exceptions import ResourceExists
from src.models import Dataset, DatasetDwhType


class DatasetRepository:

	# TODO result as kind of DTO object, instead of dict?
	@staticmethod
	def create(name: str, title: str, ref: dict) -> dict:
		try:
			dataset = Dataset(name, "dataset", title)
			dataset.save()

			dataset_dwh_type = DatasetDwhType(
				ref.get('type'), ref.get('subtype'), ref.get('table'), ref.get('primaryKey'),
				ref.get('properties'), dataset.id)
			dataset_dwh_type.save()

			print(dataset)
			print(dataset_dwh_type)

			result = {
				'id': dataset.id,
				'name': dataset.name,
				'type': 'dataset',
				'title': dataset.title,
				# 'ref': dataset.ref
			}
		except IntegrityError:
			Dataset.rollback()
			raise ResourceExists('Dataset name=' + name + ' already exists.')

		return result

	@staticmethod
	def get(name: str) -> dict:
		dataset = Dataset.query.filter_by(name=name).first_or_404()
		dataset = {
			'id': dataset.id,
			'name': dataset.name,
			'type': 'dataset',
			'title': dataset.title,
			# 'ref': dataset.ref
		}
		return dataset
