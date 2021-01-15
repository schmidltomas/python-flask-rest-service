from . import db
from .base_model import BaseModel
from src import utils


class Dataset(db.Model, BaseModel):
	__tablename__ = 'dataset'

	id = db.Column(db.String(16), primary_key=True)
	name = db.Column(db.String, unique=True)
	# TODO should be db.Integer & enum
	type = db.Column(db.String)
	title = db.Column(db.String)

	ref = db.relationship('DatasetDwhType', back_populates='dataset', uselist=False)

	def __init__(self, name, type, title):
		self.id = utils.generate_id()
		self.name = name
		self.type = type
		self.title = title

	def __repr__(self):
		return '<Dataset {},{},{}>'.format(self.id, self.name, self.ref)
