from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


def create_app(env=None):
	app = Flask(__name__)
	app.config.from_object(Config)
	db = SQLAlchemy(app)
	db.init_app(app)
	return app
