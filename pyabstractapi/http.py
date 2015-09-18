import urllib.request
import urllib.parse
import json
from functools import partial


class Methods(object):
	def __init__(self, url, resource, apiinfo=None):
		self.url = url
		self.resource = resource
		if apiinfo:
			self.apiinfo = dict(apiinfo)
		else:
			self.apiinfo = {}
		self.headers = {"Content-Type": "application/json", "Accept": "*/*", "User-Agent": "Mozilla/5.0"}

	def request(self, resource, method, body):
		meth = method.upper()

		def encode_fn(*args):
			return urllib.parse.urlencode(*args)

		data = encode_fn(body)
		if meth == "GET" or meth == "DELETE":
			return urllib.request.Request(url="{0}/{1}?{2}".format(self.url, resource, data), method=meth, headers=self.headers)
		else:
			return urllib.request.Request(url=self.url + resource, method=meth, headers=self.headers, data=data.encode("UTF-8"))

	def __req(self, method, **kwargs):
		body = dict(self.apiinfo)
		body.update(**kwargs)
		req = self.request(method=method, resource=self.resource, body=body)
		print(req.full_url)
		with urllib.request.urlopen(req) as f:
			return json.loads(f.read().decode("UTF-8"))

	def __getattr__(self, item):
		return partial(self.__req, item)
