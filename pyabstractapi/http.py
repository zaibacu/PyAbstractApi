import http.client
import json
from functools import partial


class Methods(object):
	def __init__(self, url, resource, apiinfo=None):
		if "https" in url:
			self.connection = lambda: http.client.HTTPSConnection(url)
		else:
			self.connection = lambda: http.client.HTTPConnection(url)

		self.resource = resource
		self.apiinfo = dict(apiinfo)
		self.headers = {"Content-Type": "application/json"}

	def __req(self, method, **kwargs):
		conn = self.connection()
		body = dict(self.apiinfo)
		body.update(**kwargs)
		conn.request(method, self.resource, body=json.dumps(body), headers=self.headers)
		result = conn.getresponse().read()
		conn.close()
		return result

	def __getattr__(self, item):
		return partial(self.__req, item)
