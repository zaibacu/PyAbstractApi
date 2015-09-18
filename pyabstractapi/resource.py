from pyabstractapi.http import Methods


class Resource(object):
	def __init__(self, name, parent=None):
		self.name = name
		self.branches = {}
		self.parent = parent
		# Overwrite these:
		self.url = ""
		self.apiinfo = {}

	def add_resource(self, res):
		self.branches[res.name] = res
		res.parent = self

	def get_path(self):
		if self.parent:
			return [self.name] + self.parent.get_path()
		else:
			return [self.name]

	def __call__(self):
		return Methods(self.url, "/".join(self.get_path()), self.apiinfo)

	def __getattr__(self, item):
		if self.name == item:
			return self
		elif item in self.branches.keys():
			return self.branches[item]
		else:
			raise ValueError("method '{0}' not found".format(item))
