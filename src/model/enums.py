from enum import Enum


class ExtendedEnum(Enum):

	@classmethod
	def values(cls):
		return tuple(map(lambda c: c.value, cls))


class MdObjectType(ExtendedEnum):
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


class DatasetType(ExtendedEnum):
	DWH = "dwh"
	VT = "vt"


class DatasetSubtype(ExtendedEnum):
	BASIC = "basic"
	DATE = "date"
	GEOMETRY_POINT = "geometryPoint"
	GEOMETRY_POLYGON = "geometryPolygon"
	GEOMETRY_LINE = "geometryLine"
