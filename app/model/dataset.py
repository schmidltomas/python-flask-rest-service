from marshmallow import post_load

from .md_object import MdObject, MdObjectSchema
from .md_object_type import MdObjectType


class Dataset(MdObject):
	def __init__(self, name, title, content):
		super(Dataset, self).__init__(name, MdObjectType.DATASET, title, content)
		# TODO type MdObjectType.DATASET
		# TypeError: __init__() got an unexpected keyword argument 'type'
		# TODO optional fields
		# marshmallow.exceptions.ValidationError: {'description': ['Unknown field.']}

	def __repr__(self):
		return '<Indicator(name={self.description!r})>'.format(self=self)


class DatasetSchema(MdObjectSchema):
	@post_load
	def create_indicator(self, data, **kwargs):
		return Dataset(**data)
