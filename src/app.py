from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
# from config import get_config

# db = SQLAlchemy()


def create_app(env=None):
	app = Flask(__name__)
	app.config.from_object(Config)
	db = SQLAlchemy(app)
	migrate = Migrate(app, db)

	db.init_app(app)
	return app
