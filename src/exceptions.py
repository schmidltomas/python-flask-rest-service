from datetime import datetime


class ResourceException(Exception):
	def __init__(self, message, status_code=None, payload=None):
		Exception.__init__(self)
		self.message = message
		if status_code is not None:
			self.status_code = status_code
		self.payload = payload

	def to_dict(self):
		rv = dict(self.payload or ())
		rv['status'] = self.status_code
		rv['message'] = self.message
		rv['timestamp'] = datetime.now().isoformat()
		return rv


class ResourceExists(ResourceException):
	status_code = 409


class ResourceNotFound(ResourceException):
	status_code = 404


class InvalidResource(ResourceException):
	status_code = 400
