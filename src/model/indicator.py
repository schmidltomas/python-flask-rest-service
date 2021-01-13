from marshmallow import post_load

from .md_object import MdObject, MdObjectSchema
from .md_object_type import MdObjectType


class Indicator(MdObject):
	def __init__(self, name, title, content):
		super(Indicator, self).__init__(name, MdObjectType.INDICATOR, title, content)
		# TODO type
		# TypeError: __init__() got an unexpected keyword argument 'type'
		# TODO optional fields
		# marshmallow.exceptions.ValidationError: {'description': ['Unknown field.']}

	def __repr__(self):
		return '<Indicator(name={self.description!r})>'.format(self=self)


class IndicatorSchema(MdObjectSchema):
	@post_load
	def create_indicator(self, data, **kwargs):
		return Indicator(**data)
