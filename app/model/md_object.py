from marshmallow import Schema, fields


class MdObject:
	def __init__(self, name, type, title, content):
		self.name = name
		self.type = type
		self.title = title
		self.content = content

	def __repr__(self):
		return '<Dataset(name={self.description!r})>'.format(self=self)


class MdObjectSchema(Schema):
	name = fields.Str()
	type = fields.Str()
	title = fields.Str()
	content = fields.Dict()
