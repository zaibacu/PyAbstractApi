import unittest
from pyabstractapi.resource import Resource, Methods


class ResourceTests(unittest.TestCase):
	def test_method_calling(self):
		class Res(Resource):
			pass

		res1 = Res("res1")
		res2 = Res("res2")
		res3 = Res("res3")
		res4 = Res("res4")
		res1.add_resource(res2)
		res1.add_resource(res3)
		res3.add_resource(res4)

		self.assertTrue(isinstance(res1.res1(), Methods))
		self.assertTrue(isinstance(res1.res2(), Methods))
		self.assertTrue(isinstance(res1.res3.res4(), Methods))

