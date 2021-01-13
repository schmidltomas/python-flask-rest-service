from enum import Enum


class MdObjectType(Enum):
	DATASET = "dataset"
	VIEW = "view"
	DASHBOARD = "dashboard"
	INDICATOR_DRILL = "indicatorDrill"
	INDICATOR = "indicator"
	METRIC = "metric"
	MARKER = "marker"
	MARKER_SELECTOR = "markerSelector"
	EXPORT = "export"
	DATA_PERMISSION = "dataPermission"
	PROJECT_SETTINGS = "projectSettings"
	SHARE = "share"
