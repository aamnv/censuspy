import requests
from urllib import parse

class bds(object):

	BASE_URL = 'https://api.census.gov/data/timeseries/bds/firms?'

	def __init__(self, api_key=None, geo=None):
		if (api_key == None or geo == None):
			raise ValueError('Missing api_key or geo parameters.')

		else:
			self.api_key = api_key
			self.geo = '&' + parse.urlencode({'for': geo}) + ':'

	def get(self, metric=None, time=None, code='*', sic1=0, fage4='m', fsize='m', ifsize='m'):		
		if (metric == None or time == None):
			raise ValueError('Missing metric and/or time parameters.')

		else:
			self.code = str(code)
			self.metric = 'get=' + metric
			self.params_dict = {

				'time': str(time), 'sic1': str(sic1), 'fage4': fage4,
				'fsize': fsize, 'ifsize': ifsize, 'key': self.api_key

				}

		return self._basic_execution()

	def _url_builder(self, base_url, metric):
		return base_url + metric + self.geo + self.code + '&' + parse.urlencode(self.params_dict)

	def _make_request(self, url):
		try:
			r = requests.get(url)
			status = r.status_code

			if status == 204:
				return None

			elif status == 200:
				return r.json()

			else:
				return 'ERROR: ' + str(status)

		except:
			raise ValueError('Incorrect parameters led to invalid API call.')

	def _basic_execution(self):
		if (self.geo == '&for=state:' and self.code == '*'):
			raise ValueError('Missing code parameter.')

		else:
			url = self._url_builder(self.BASE_URL, self.metric)
			json = self._make_request(url)

			try:
				if json == None:
					return 'N/A'

				elif json[:5] == 'ERROR':
					return json

				else:
					return json[1][0]

			except:
				return 'UNKN ERROR'