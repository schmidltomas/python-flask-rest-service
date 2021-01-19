import os
import exrex
import json


def get_env_variable(name) -> str:
	try:
		return os.environ[name]
	except KeyError:
		message = "Expected environment variable '{}' not set.".format(name)
		raise Exception(message)


def generate_id() -> str:
	return exrex.getone('[a-z]{1}[a-z0-9]{15}')


def read_file(filename):
	with open(filename, "r") as file:
		return json.loads(file.read())


def path_to_str(path_list):
	path = "'$"

	for item in path_list:
		path += "."
		if isinstance(item, int):
			path += "[" + str(item) + "]"
		else:
			path += str(item)

	return path
