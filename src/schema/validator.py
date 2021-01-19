from jsonschema import Draft7Validator
from ..exceptions import InvalidResource
from src import utils


class Validator(object):
	def __init__(self, schema):
		self.schema = utils.read_file(schema)

	def validate(self, json):
		validator = Draft7Validator(self.schema)
		errors = sorted(validator.iter_errors(json), key=str)
		if len(errors) > 0:
			path = utils.path_to_str(errors[0].path)
			message = str(errors[0].message)
			raise InvalidResource("Field " + path + "' with value " + message + ".")
