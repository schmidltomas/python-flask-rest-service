from marshmallow import post_load

from .md_object import MdObject, MdObjectSchema
from .md_object_type import MdObjectType


class Marker(MdObject):
	def __init__(self, name, title, content):
		super(Marker, self).__init__(name, MdObjectType.MARKER, title, content)

	def __repr__(self):
		return '<Marker(name={self.description!r})>'.format(self=self)


class MarkerSchema(MdObjectSchema):
	@post_load
	def create_marker(self, data, **kwargs):
		return Marker(**data)
