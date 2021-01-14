from . import db
from .base_model import BaseModel
from src import utils
from sqlalchemy.dialects.postgresql import JSON


class DatasetDwhType(db.Model, BaseModel):
	__tablename__ = 'dataset_dwh_type'

	id = db.Column(db.String(16), primary_key=True)
	type = db.Column(db.String(8))
	subtype = db.Column(db.String(16))
	table = db.Column(db.String(64))
	primary_key = db.Column(db.String(32))
	properties = db.Column(JSON)
	dataset_id = db.Column(db.String(16), db.ForeignKey('dataset.id'))

	def __init__(self, type, subtype, table, primary_key, properties, dataset_id):
		self.id = utils.generate_id()
		self.type = type
		self.subtype = subtype
		self.table = table
		self.primary_key = primary_key
		self.properties = properties
		self.dataset_id = dataset_id

	def __repr__(self):
		return '<DatasetDwhType {}>'.format(self.id)
