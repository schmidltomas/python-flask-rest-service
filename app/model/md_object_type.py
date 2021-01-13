from enum import Enum


class MdObjectType(Enum):
	DASHBOARD = "dashboard"
	DATA_PERMISSION = "dataPermission"
	DATASET = "dataset"
	EXPORT = "export"
	INDICATOR = "indicator"
	INDICATOR_DRILL = "indicatorDrill"
	MARKER = "marker"
	MARKER_SELECTOR = "markerSelector"
	METRIC = "metric"
	PROJECT_SETTINGS = "projectSettings"
	SHARE = "share"
	VIEW = "view"
