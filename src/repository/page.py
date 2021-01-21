from flask_sqlalchemy import Pagination


def link(rel: str, page: int, size: int):
	return {
		'rel': rel,
		'href': '/datasets?page=' + str(page) + '&size=' + str(size)
	}


class Page:

	def __init__(self, page: Pagination, objects: dict):
		self.size = page.per_page
		self.total_elements = page.total
		self.total_pages = page.total // page.per_page + 1
		self.number = page.page
		self.objects = objects
		self.links = []

		self.links.append(link('self', page.page, page.per_page))
		if page.has_next:
			self.links.append(link('next', page.page + 1, page.per_page))
		if page.has_prev:
			self.links.append(link('prev', page.page - 1, page.per_page))

	def to_page(self):
		return {
			'page': {
				'size': self.size,
				'totalElements': self.total_elements,
				'totalPages': self.total_pages,
				'number': self.number
			},
			'links': self.links,
			'content': self.objects
		}
