About
=====
Simple Framework for creating nested API structures working on RestFul principle

Example
=======
```
from pyabstractapi.resource import Resource
class MyApi(Resource):
	def __init__(self, name):
		super(self, MyApi).__init__(name)
		self.url = "https://my-api.com/v3/"
		self.apiinfo = {"api_key": "123XYZ"}

users = MyApi("users")
search = MyApi("search")
users.add_resource(search)

search.get(first_name="John", last_name="Smith")
```