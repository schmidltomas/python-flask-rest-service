from src import ma
from src.model import Dataset
from .dataset_dwh_type_schema import DatasetDwhTypeSchema
from .base_schema import BaseSchema


class DatasetSchema(ma.SQLAlchemySchema, BaseSchema):
	class Meta:
		model = Dataset
		fields = ('id', 'name', 'type', 'title', 'ref')
		ordered = True

	ref = ma.Nested(DatasetDwhTypeSchema)
