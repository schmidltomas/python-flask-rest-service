from . import db
from .base_model import BaseModel
from .enums import MdObjectType
from src import utils


class Dataset(db.Model, BaseModel):
	__tablename__ = 'dataset'

	id = db.Column(db.String(16), primary_key=True)
	name = db.Column(db.String, unique=True)
	type = db.Column(db.Enum(*MdObjectType.values(), name='type', create_type=False))
	title = db.Column(db.String)

	ref = db.relationship('DatasetDwhType', back_populates='dataset', uselist=False, passive_deletes=True)

	def __init__(self, name, object_type, title):
		self.id = utils.generate_id()
		self.name = name
		self.type = object_type
		self.title = title

	def __repr__(self):
		return '<Dataset {},{},{}>'.format(self.id, self.name, self.ref)
