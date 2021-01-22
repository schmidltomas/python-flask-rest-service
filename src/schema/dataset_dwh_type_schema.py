from src import ma
from src.model import DatasetDwhType
from .base_schema import BaseSchema


class DatasetDwhTypeSchema(ma.SQLAlchemySchema, BaseSchema):
	class Meta:
		model = DatasetDwhType
		fields = ('type', 'subtype', 'table', 'primary_key', 'categorizable', 'properties')
		ordered = True
