from . import db
from .base_model import BaseModel
from .enums import DatasetType, DatasetSubtype
from src import utils
from sqlalchemy.dialects.postgresql import JSON


class DatasetDwhType(db.Model, BaseModel):
	__tablename__ = 'dataset_dwh_type'

	id = db.Column(db.String(16), primary_key=True)
	type = db.Column(db.Enum(*DatasetType.values(), name='dataset_type', create_type=False))
	subtype = db.Column(db.Enum(*DatasetSubtype.values(), name='dataset_subtype', create_type=False))
	table = db.Column(db.String)
	primary_key = db.Column(db.String)
	categorizable = db.Column(db.Boolean)
	properties = db.Column(JSON)

	dataset_id = db.Column(db.String(16), db.ForeignKey('dataset.id', ondelete='CASCADE'))
	dataset = db.relationship('Dataset', back_populates='ref')

	def __init__(self, dataset_type, subtype, table, primary_key, categorizable, properties, dataset_id):
		self.id = utils.generate_id()
		self.type = dataset_type
		self.subtype = subtype
		self.table = table
		self.primary_key = primary_key
		self.categorizable = categorizable
		self.properties = properties
		self.dataset_id = dataset_id

	def __repr__(self):
		return '<DatasetDwhType {}>'.format(self.id)
