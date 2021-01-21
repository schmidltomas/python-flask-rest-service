from . import db
from typing import List
from flask_sqlalchemy import Pagination
from werkzeug.exceptions import NotFound


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

	@classmethod
	def find_page(cls, page: int, size: int):
		try:
			return cls.query.paginate(page=page, per_page=size)
		except NotFound:
			# return empty page instead of exception with 404 by raised paginate()
			query_all = cls.query.all()
			return Pagination(query_all, page, size, len(query_all), list())

	@staticmethod
	def rollback():
		db.session.rollback()

	@staticmethod
	def commit():
		db.session.commit()
