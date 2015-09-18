import urllib.request
import json
from functools import partial


class Methods(object):
	def __init__(self, url, resource, https=True, apiinfo=None):
		self.url = url
		self.resource = resource
		self.apiinfo = dict(apiinfo)
		self.headers = {"Content-Type": "application/json", "Accept": "*/*"}

	def request(self, resource, method, body):
		return urllib.request.Request(url=self.url + resource, method=method.upper(), data=json.dumps(body).encode("utf-8"))

	def __req(self, method, **kwargs):
		body = dict(self.apiinfo)
		body.update(**kwargs)
		req = self.request(method=method, resource=self.resource, body=body)
		with urllib.request.urlopen(req) as f:
			return f.read()

	def __getattr__(self, item):
		return partial(self.__req, item)
