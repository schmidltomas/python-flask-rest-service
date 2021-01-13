from app import db
from sqlalchemy.dialects.postgresql import JSON


class Dataset(db.Model):
	__tablename__ = 'dataset'

	id = db.Column(db.String(16), primary_key=True)
	name = db.Column(db.String(256), unique=True)
	type = db.Column(db.String(256))
	title = db.Column(db.String(1024))
	ref = db.relationship('DatasetDwhType', backref='dataset', lazy='dynamic')

	def __init__(self, name, type, title, ref):
		self.name = name
		self.type = type
		self.title = title
		self.ref = ref

	def __repr__(self):
		return '<Dataset {}>'.format(self.id)


class DatasetDwhType(db.Model):
	__tablename__ = 'dataset_dwh_type'

	id = db.Column(db.String(16), primary_key=True)
	type = db.Column(db.String(8))
	subtype = db.Column(db.String(16))
	table = db.Column(db.String(64))
	primary_key = db.Column(db.String(32))
	properties = db.Column(JSON)
	dataset_id = db.Column(db.String(16), db.ForeignKey('dataset.id'))

	def __init__(self, type, subtype, table, primary_key, properties):
		self.type = type
		self.subtype = subtype
		self.table = table
		self.primary_key = primary_key
		self.properties = properties

	def __repr__(self):
		return '<DatasetDwhType {}>'.format(self.id)
