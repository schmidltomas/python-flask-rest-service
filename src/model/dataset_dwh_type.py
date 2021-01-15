from . import db
from .base_model import BaseModel
from src import utils
from sqlalchemy.dialects.postgresql import JSON


class DatasetDwhType(db.Model, BaseModel):
	__tablename__ = 'dataset_dwh_type'

	id = db.Column(db.String, primary_key=True)
	# TODO should be db.Integer & enum
	type = db.Column(db.String)
	# TODO should be db.Integer & enum
	subtype = db.Column(db.String)
	table = db.Column(db.String)
	primary_key = db.Column(db.String)
	properties = db.Column(JSON)

	dataset_id = db.Column(db.String(16), db.ForeignKey('dataset.id'))
	dataset = db.relationship('Dataset', back_populates='ref')

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
