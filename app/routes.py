from flask import Flask, jsonify, request

from app.model.dataset import Dataset, DatasetSchema
from app.model.md_object_type import MdObjectType

app = Flask(__name__)

md_objects = []


@app.route("/datasets")
def get_datasets():
	schema = DatasetSchema(many=True)
	datasets = schema.dump(
		filter(lambda t: t.type == MdObjectType.DATASET, md_objects)
	)
	return jsonify(datasets)


@app.route('/dataset', methods=['POST'])
def add_dataset():
	dataset = DatasetSchema().load(request.get_json())
	md_objects.append(dataset)
	return '', 204
