import requests

class bds(object):

	BASE_URL = 'https://api.census.gov/data/timeseries/bds/firms'

	def __init__(self, api_key=None, geo=None, time=None, sic1=0):
		if (api_key == None or geo == None or time == None):
			raise ValueError('Missing api_key, geo, or time dimension.')

		else:
			self.api_key = '&key=' + api_key
			self.geo = '&for=' + geo + ':'
			self.time = '&time=' + str(time)
			self.sic1 = '&sic1=' + str(sic1)

	def emp(self, code=None):		
		self.get_value = '?get=emp'
		self.code = code

		return self._execute_request()

	def estabs(self, code=None):		
		self.get_value = '?get=estabs'
		self.code = code

		return self._execute_request()

	def firms(self, code=None):		
		self.get_value = '?get=firms'
		self.code = code

		return self._execute_request()

	def job_creation(self, code=None):		
		self.get_value = '?get=job_creation'
		self.code = code

		return self._execute_request()

	def job_destruction(self, code=None):		
		self.get_value = '?get=job_destruction'
		self.code = code

		return self._execute_request()

	def _url_builder(self, base_url, get_value):
		other_params = self.time + self.sic1 + self.api_key
		return base_url + get_value + self.geo + self.code + other_params

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

	def _execute_request(self):
		if self.geo == 'us':
			pass

		else:
			if self.code == None:
				raise ValueError('Missing code or state dimension.')

			else:
				url = self._url_builder(self.BASE_URL, self.get_value)
				json = self._make_request(url)

				try:
					return json[1][0]

				except:
					return json
					pass
