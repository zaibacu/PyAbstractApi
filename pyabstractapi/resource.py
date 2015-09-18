from pyabstractapi.http import Methods


class Resource(object):
	def __init__(self, name):
		self.name = name
		self.branches = {}
		self.parent = None
		# Overwrite these:
		self.url = ""
		self.apiinfo = {}

	def add_resource(self, res):
		self.branches[res.name] = res
		res.parent = self

	def get_path(self):
		if self.parent:
			return self.parent.get_path() + ["{0}.json".format(self.name)]
		else:
			return [self.name]

	def __call__(self):
		return Methods(self.url, "/".join(self.get_path()), self.apiinfo)

	def __getattr__(self, item):
		http = {"get", "put", "post", "delete", "head"}
		if item in http:
			methods = Methods(self.url, "/".join(self.get_path()), self.apiinfo)
			return getattr(methods, item)
		elif item in self.branches.keys():
			return self.branches[item]
		else:
			return object.__getattribute__(self, item)
