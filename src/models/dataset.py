from . import db
from .base_model import BaseModel
from src import utils


class Dataset(db.Model, BaseModel):
	__tablename__ = 'dataset'

	id = db.Column(db.String(16), primary_key=True)
	name = db.Column(db.String(256), unique=True)
	type = db.Column(db.String(256))
	title = db.Column(db.String(1024))
	ref = db.relationship('DatasetDwhType', backref='dataset', lazy='dynamic')

	def __init__(self, name, type, title):
		self.id = utils.generate_id()
		self.name = name
		self.type = type
		self.title = title

	def __repr__(self):
		return '<Dataset {}>'.format(self.id)
