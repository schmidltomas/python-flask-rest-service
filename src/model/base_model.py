from . import db
from typing import List


class BaseModel:
	def save(self):
		db.session.add(self)
		db.session.commit()
		return self

	def update(self, schema):
		for key, value in schema.items():
			if hasattr(self, key) and not isinstance(value, dict):
				setattr(self, key, value)

		db.session.commit()
		return self

	def delete(self):
		db.session.delete(self)
		db.session.commit()
		return self

	@classmethod
	def find_by_id(cls, _id: str) -> "BaseModel":
		return cls.query.filter_by(id=_id).first()

	@classmethod
	def find_by_name(cls, _name: str) -> "BaseModel":
		return cls.query.filter_by(name=_name).first()

	@classmethod
	def find_all(cls) -> List["BaseModel"]:
		return cls.query.all()

	@staticmethod
	def rollback():
		db.session.rollback()

	@staticmethod
	def commit():
		db.session.commit()
