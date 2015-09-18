from pyabstractapi.http import Methods


class Resource(object):
	def __init__(self, name):
		self.name = name
		self.branches = {}
		self.parent = None
		# Overwrite these:
		self.url = ""
		self.apiinfo = {}
		self.https = True

	def add_resource(self, res):
		self.branches[res.name] = res
		res.parent = self

	def get_path(self):
		if self.parent:
			return self.parent.get_path() + [self.name]
		else:
			return ["", self.name]

	def __call__(self):
		return Methods(self.url, "/".join(self.get_path()), self.https, self.apiinfo)

	def __getattr__(self, item):
		if self.name == item:
			return self
		elif item in self.branches.keys():
			return self.branches[item]
		else:
			raise ValueError("method '{0}' not found".format(item))
