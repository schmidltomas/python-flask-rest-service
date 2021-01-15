from src import ma
from src.model import Dataset
from .dataset_dwh_type_schema import DatasetDwhTypeSchema


class DatasetSchema(ma.SQLAlchemySchema):
	class Meta:
		model = Dataset
		fields = ('id', 'name', 'title', 'ref')
		ordered = True

	ref = ma.Nested(DatasetDwhTypeSchema)
