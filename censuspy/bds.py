import requests
from urllib import parse

class bds(object):

	BASE_URL = 'https://api.census.gov/data/timeseries/bds/firms?'

	def __init__(self, api_key=None, geo=None):
		if (api_key == None or geo == None):
			raise ValueError('Missing api_key or geo parameters.')

		else:
			self.api_key = api_key
			self.geo = '&for=' + geo + ':'

	def get(self, metric=None, code=None, time=None, sic1=0, fage4='m', fsize='m', ifsize='m'):		
		if (metric == None or code == None or time == None):
			raise ValueError('Missing metric, code, and/or time parameters.')

		else:
			self.code = str(code)
			self.metric = 'get=' + metric
			self.params_dict = {

								'time': str(time),
								'sic1': str(sic1),
								'fage4': fage4,
								'fsize': fsize,
								'ifsize': ifsize,
								'key': self.api_key

								}

		return self._basic_execution()

	def _url_builder(self, base_url, metric):
		return base_url + metric + self.geo + self.code + '&' + parse.urlencode(self.params_dict)

	def _make_request(self, url):
		try:
			r = requests.get(url)
			status = r.status_code

			if status == 204:
				return 'N/A'

			elif status == 200:
				return r.json()

			else:
				return str(status)

		except:
			raise ValueError('Incorrect parameters led to invalid API call.')

	def _basic_execution(self):
		if self.geo == 'us':
			pass

		else:
			if self.code == None:
				raise ValueError('Missing code or state dimension.')

			else:
				url = self._url_builder(self.BASE_URL, self.metric)
				json = self._make_request(url)

				try:
					return json[1][0]

				except:
					return json
					pass
