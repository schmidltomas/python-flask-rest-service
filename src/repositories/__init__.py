from flask_sqlalchemy import SQLAlchemy
from .dataset import DatasetRepository


db = SQLAlchemy()
__all__ = ['DatasetRepository']
