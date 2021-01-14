import os
import exrex


def get_env_variable(name) -> str:
	try:
		return os.environ[name]
	except KeyError:
		message = "Expected environment variable '{}' not set.".format(name)
		raise Exception(message)


def generate_id() -> str:
	return exrex.getone('[a-z]{1}[a-z0-9]{15}')
