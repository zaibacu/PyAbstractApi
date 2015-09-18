from pyabstractapi.http import Methods

class Resource(object):
	def __init__(self, name):
		self.name = name
		self.branches = {}

	def add_resource(self, res):
		self.branches[res.name] = res

	def __call__(self):
		return Methods()

	def __getattr__(self, item):
		if self.name == item:
			return self
		elif item in self.branches.keys():
			return self.branches[item]
		else:
			raise ValueError("method '{0}' not found".format(item))
