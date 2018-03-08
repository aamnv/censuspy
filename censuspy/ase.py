import requests
from urllib import parse

class csa(object):

	BASE_URL = 'https://api.census.gov/data/2014/ase/csa?'

	def __init__(self, api_key=None, geo=None):
		if (api_key == None or geo == None):
			raise ValueError('Missing api_key or geo parameters.')

		else:
			self.api_key = api_key
			self.geo = '&' + parse.urlencode({'for': geo}) + ':'

	def get(self, metric=None, code='*', empszfi=None, rcpszfi=None, sex=None, vet_group=None,
			naics2012=None, yibszfi=None, eth_group=None, race_group=None):		
		if (metric == None or code == None):
			raise ValueError('Missing metric and/or code parameters.')

		else:
			self.code = str(code)
			metric = metric.upper()
			self.metric = 'get=' + metric
			self.raw_params_dict = {

				'EMPSZFI': str(empszfi), 'RCPSZFI': str(rcpszfi), 'SEX': str(sex),
				'VET_GROUP': str(vet_group), 'NAICS2012': str(naics2012), 'YIBSZFI': str(yibszfi),
				'ETH_GROUP': str(eth_group), 'RACE_GROUP': str(race_group), 'key': self.api_key

				}

		self.params_dict = {}
		for k, v in self.raw_params_dict.items():
			if v == 'None':
				pass

			else:
				self.params_dict.update({k:v})

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

class cscb(object):

	BASE_URL = 'https://api.census.gov/data/2014/ase/cscb?'

	def __init__(self, api_key=None, geo=None):
		if (api_key == None or geo == None):
			raise ValueError('Missing api_key or geo parameters.')

		else:
			self.api_key = api_key
			self.geo = '&' + parse.urlencode({'for': geo}) + ':'

	def get(self, metric=None, code='*', acqbuscap=None, asecb=None, avoidfinan=None, benefits=None,
			busact=None, busaspir=None, busoutus=None, ceaseops=None, cust=None, custlocpct=None, famown=None,
			fundsrc=None, innovimp=None, intelctprop=None, lang=None, naics2012=None, negprofit=None, 
			newfundrel=None, opfran=None, outsrcus=None, ownrnum=None, pecommrc=None, pexport=None, profit=None,
			rdpuramt=None, rdtotalcst=None, rdworkers=None, spouses=None, strtsrce=None, website=None, workers=None,
			yibszfi=None, yrestbus=None):		
		if (metric == None or code == None):
			raise ValueError('Missing metric and/or code parameters.')

		else:
			self.code = str(code)
			metric = metric.upper()
			self.metric = 'get=' + metric
			self.raw_params_dict = {

				'ACQBUSCAP': str(acqbuscap), 'ASECB': str(asecb), 'AVOIDFINAN': str(avoidfinan),						
				'BENEFITS': str(benefits), 'BUSACT': str(busact), 'BUSASPIR': str(busaspir),
				'BUSOUTUS': str(busoutus), 'CEASEOPS': str(ceaseops), 'CUST': str(cust),
				'CUSTLOCPCT': str(custlocpct), 'FAMOWN': str(famown), 'FUNDSRC': str(fundsrc),
				'INNOVIMP': str(innovimp), 'INTELCTPROP': str(intelctprop), 'LANG': str(lang),
				'NAICS2012': str(naics2012), 'NEGPROFIT': str(negprofit), 'NEWFUNDREL': str(newfundrel),
				'OPFRAN': str(opfran), 'OUTSRCUS': str(outsrcus), 'OWNRNUM': str(ownrnum),
				'PECOMMRC': str(pecommrc), 'PEXPORT': str(pexport), 'PROFIT': str(profit),
				'RDPURAMT': str(rdpuramt), 'RDTOTALCST': str(rdtotalcst), 'RDWORKERS': str(rdworkers),
				'SPOUSES': str(spouses), 'STRTSRCE': str(strtsrce), 'WEBSITE': str(website),
				'WORKERS': str(workers), 'YIBSZFI': str(yibszfi), 'YRESTBUS': str(yrestbus), 'key': self.api_key

				}

		self.params_dict = {}
		for k, v in self.raw_params_dict.items():
			if v == 'None':
				pass

			else:
				self.params_dict.update({k:v})

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

class cscbo(object):

	BASE_URL = 'https://api.census.gov/data/2014/ase/cscbo?'

	def __init__(self, api_key=None, geo=None):
		if (api_key == None or geo == None):
			raise ValueError('Missing api_key or geo parameters.')

		else:
			self.api_key = api_key
			self.geo = '&' + parse.urlencode({'for': geo}) + ':'

	def get(self, metric=None, code='*', acqbus=None, asecbo=None, educ=None, hrswrkd=None, naics2012=None,
		ownrage=None, pfnct=None, priorbus=None, prminc=None, usborncit=None, yracqbus=None):		
		if (metric == None or code == None):
			raise ValueError('Missing metric and/or code parameters.')

		else:
			self.code = str(code)
			metric = metric.upper()
			self.metric = 'get=' + metric
			self.raw_params_dict = {

				'ACQBUS': str(acqbus), 'ASECBO': str(asecbo), 'EDUC': str(educ), 'HRSWRKD': str(hrswrkd), 
				'NAICS2012': str(naics2012), 'OWNRAGE': str(ownrage), 'PFNCT': str(pfnct), 'PRIORBUS': str(priorbus),
				'PRMINC': str(prminc), 'USBORNCIT': str(usborncit), 'YRACQBUS': str(yracqbus), 'key': self.api_key

				}

		self.params_dict = {}
		for k, v in self.raw_params_dict.items():
			if v == 'None':
				pass

			else:
				self.params_dict.update({k:v})

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
