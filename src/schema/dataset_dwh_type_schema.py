from src import ma
from src.model import DatasetDwhType


class DatasetDwhTypeSchema(ma.SQLAlchemySchema):
	class Meta:
		model = DatasetDwhType
		fields = ('type', 'subtype', 'table', 'primary_key', 'properties')
		ordered = True
