from flask import Flask, jsonify, request

from src.model.indicator import Indicator, IndicatorSchema
from src.model.marker import Marker, MarkerSchema
from src.model.md_object_type import MdObjectType

app = Flask(__name__)

md_objects = [
	# Indicator("turnover_indicator", "Turnover indicator", {
	# 	"scale": "standard", "distribution": "geometric", "visualizations":
	# 		{"heatmap": True, "dominance": True}}),
	# Marker("store_marker", "Stores", {"style": "marker-orange", "propertyFilters": [
	# 	{"propertyName": "partner", "value": "no", "operator": "eq"}
	# ]})
]


@app.route("/indicators")
def get_indicators():
	schema = IndicatorSchema(many=True)
	indicators = schema.dump(
		filter(lambda t: t.type == MdObjectType.INDICATOR, md_objects)
	)
	return jsonify(indicators)


@app.route('/indicators', methods=['POST'])
def add_indicator():
	indicator = IndicatorSchema().load(request.get_json())
	md_objects.append(indicator)
	return '', 204


@app.route("/markers")
def get_markers():
	schema = MarkerSchema(many=True)
	markers = schema.dump(
		filter(lambda t: t.type == MdObjectType.MARKER, md_objects)
	)
	return jsonify(markers)


@app.route('/markers', methods=['POST'])
def add_marker():
	marker = MarkerSchema().load(request.get_json())
	md_objects.append(marker)
	return '', 204
