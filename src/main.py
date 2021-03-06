from flask_restful import Api
from src.resource import Dataset, DatasetList, HealthCheck
from src.model import db
from flask_migrate import Migrate
from .app import create_app

app = create_app()
migrate = Migrate(app, db)

api = Api(app)
api.add_resource(HealthCheck, '/healthcheck')
api.add_resource(Dataset, '/datasets/<id>')
api.add_resource(DatasetList, '/datasets')


# TODO:
#  - improve health check with DB availability
#  - ETags, object versioning
#  - docstrings/comments
#  - move JSON validation to decorator
