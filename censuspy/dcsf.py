import requests
from urllib import parse

class dcsf(object):
	def __init__(self, api_key=None, time=None):
		if (api_key == None or time == None):
			raise ValueError('Missing api_key or time parameters.')

		else:
			self.api_key = api_key
			self.time = str(time)
			self.BASE_URL = 'https://api.census.gov/data/' + self.time + '/surname?'

	def get(self, metric=None, name=None, rank=None):		
		if (metric == None or (name == None and rank == None)):
			raise ValueError('Missing metric, name, and/or rank parameters.')

		else:
			metric = metric.upper()
			self.metric = 'get=' + metric
			self.raw_params_dict = {

				'NAME': str(name), 
				'RANK': str(rank), 
				'key': self.api_key

				}

		self.params_dict = {}
		for k, v in self.raw_params_dict.items():
			if v == 'None':
				self.metric = self.metric + ',' + k

			else:
				self.params_dict.update({k:v})

		return self._basic_execution()

	def _url_builder(self, base_url, metric):
		return base_url + metric + '&' + parse.urlencode(self.params_dict)

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
		url = self._url_builder(self.BASE_URL, self.metric)
		json = self._make_request(url)
		try:
			if json == None:
				return 'N/A'

			elif json[:5] == 'ERROR':
				return json

			else:
				if json[0][1] == 'NAME':
					output_dict = {
						'metric': json[1][0],
						'name': json[1][1],
						'rank': json[1][2]
					}

				else:
					output_dict = {
						'metric': json[1][0],
						'name': json[1][2],
						'rank': json[1][1]
					}

				return output_dict
		except:
			return 'UNKN ERROR'