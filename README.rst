================
CensusPy 1.0.0
================
The goal of CensusPy is to expose the vast amount of data the government collects on US citizens to the broader programming community. Written as a wrapper around existing census APIs, CensusPy 1.0.0 currently supports:

* `Business Dynamics Statistics <https://www.census.gov/data/developers/data-sets/business-dynamics.html>`_
* `Annual Survey of Entrepreneurs <https://www.census.gov/data/developers/data-sets/ase.html>`_

But, the end goal will be to support all databases provided by the Census Bureau.

Table of Contents
=================
* Installation
* Business Dynamics Statistics (BDS)
   - BDS Overview
   - BDS Quick Start
   - Business Dynamics Statistics (BDS)
* Annual Survey of Entrepreneurs (ASE)
   - ASE Overview
   - ASE Quick Start
   - Company Summary (CSA)
   - Characteristics of Businesses (CSCB)
   - Characteristics of Business Owners (CSCBO)
* Goals & Roadmap
* Changelog
* License

Installation
===============
CensusPy is supported on PyPi, so installation is as simple as::

  pip install censuspy

CensusPy only supports Python >= 3.0

Business Dynamics Statistics (BDS)
===================================
Overview (BDS)
^^^^^^^^^^^^^^^^^^^^^
The Business Dynamics Statistics (BDS) includes measures of establishment openings and closings, firm startups, job creation and destruction by firm size, age, and industrial sector, and several other statistics on business dynamics. The BDS is made up of only one sub-dataset.

Quickstart (BDS)
^^^^^^^^^^^^^^^^^^^^^
Initialize the BDS object using your API key & geographic level of query::

  from censuspy import bds
  state = bds.bds(api_key=[YOUR_API_KEY_HERE], geo='state')

Pull total employment numbers for Massachusetts (FIPS code 25) in 2014::

  ma_emp = state.get(metric='emp', code=25, time=2014)
  print(ma_emp)

Parameters (BDS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* ``metric`` (**required**)
   - specify metric to pull
   - `full BDS variables list <https://api.census.gov/data/timeseries/bds/firms/variables.html>`_
* ``code`` (**conditionally required**)
   - specify state or metro FIPS code
   - only required if geographic level != us
   - `FIPS state codes <https://www.mcc.co.mercer.pa.us/dps/state_fips_code_listing.htm>`_
* ``time`` (**required**)
   - specify time period
   - acceptable values include 1976 - 2014
   - might not return results for every year if no data for specific geo
* ``sic1`` (optional)
   - specify industry sector
   - default = 0 (all included)
   - options listed on `BDS website <https://www.census.gov/data/developers/data-sets/business-dynamics.html>`_
* ``fage4`` (optional)
   - specify firm age
   - default = 'm' (all included)
   - options listed on `BDS website <https://www.census.gov/data/developers/data-sets/business-dynamics.html>`_
* ``fsize`` (optional)
   - specify firm size
   - default = 'm' (all included)
   - options listed on `BDS website <https://www.census.gov/data/developers/data-sets/business-dynamics.html>`_
* ``ifsize`` (optional)
   - specify **initial** firm size
   - default = 'm' (all included)
   - options listed on `BDS website <https://www.census.gov/data/developers/data-sets/business-dynamics.html>`_

Other Documentation (BDS)
^^^^^^^^^^^^^^^^^^^^^^^^^^
* `General information about the BDS database <https://www.census.gov/data/developers/data-sets/business-dynamics.html>`_
* `BDS API call examples and supported geographies <https://api.census.gov/data/timeseries/bds/firms.html>`_
* `List of available BDS metrics/variables <https://api.census.gov/data/timeseries/bds/firms/variables.html>`_
* `FIPS State Codes <https://www.mcc.co.mercer.pa.us/dps/state_fips_code_listing.htm>`_

Annual Survey of Entrepreneurs (ASE)
======================================
Overview (ASE)
^^^^^^^^^^^^^^^^^^^^^
The Annual Survey of Entrepreneurs (ASE) supplements the 5-year Survey of Business Owners (SBO) program and provides more timely updates on the status, nature, and scope of women-, minority-, and veteran-owned businesses for 2014. The ASE has three sub-datasets:

* Company Summary (CSA)
* Characteristics of Businesses (CSCB)
* Characteristics of Business Owners (CSCBO)

Quickstart (ASE)
^^^^^^^^^^^^^^^^^^^^^
Initialize the ASE object using your API key & geographic level of query, then specify the dataset that you want to access. In this example we will work with the Company Summary (CSA) dataset::

  from censuspy import ase
  state = ase.csa(api_key=[YOUR_API_KEY_HERE], geo='state')

Pull total employment numbers for Massachusetts (FIPS code 25) in 2014::

  ma_emp = state.get(metric='emp', code=25)
  print(ma_emp)

Overview (CSA)
^^^^^^^^^^^^^^^^^^^^^
Provides data for employer businesses by sector, gender, ethnicity, race, veteran status, years in business, receipts size of firm, and employment size of firm for the U.S., states, and the fifty most populous metropolitan statistical areas (MSAs).

Parameters (CSA)
^^^^^^^^^^^^^^^^^^^^^
* ``metric`` (**required**)
   - specify metric to pull
   - `full CSA variables list <https://api.census.gov/data/2014/ase/csa/variables.html>`_
* ``code`` (**conditionally required**)
   - specify state or metro FIPS code
   - only required if geographic level != us
   - `FIPS state codes <https://www.mcc.co.mercer.pa.us/dps/state_fips_code_listing.htm>`_
* ``empszfi`` (optional)
   - employment size of firms
   - `options for CSA empszfi input <https://api.census.gov/data/2014/ase/csa?get=EMPSZFI,EMPSZFI_TTL&for=us:*>`_
* ``rcpszfi`` (optional)
   - sales, receipts, and revenue size of firms
   - `options for CSA rcpszfi input <https://api.census.gov/data/2014/ase/csa?get=RCPSZFI,RCPSZFI_TTL&for=us:*>`_
* ``sex`` (optional)
   - gender, ethnicity, race, and veteran status
   - `options for CSA sex input <https://api.census.gov/data/2014/ase/csa?get=SEX,SEX_TTL&for=us:*>`_
* ``vet_group`` (optional)
   - veteran group
   - `options for CSA vet_group input <https://api.census.gov/data/2014/ase/csa?get=VET_GROUP,VET_GROUP_TTL&for=us:*>`_
* ``naics2012`` (optional)
   - 2012 NAICS code
   - `options for CSA naics2012 input <https://api.census.gov/data/2014/ase/csa?get=NAICS2012,NAICS2012_TTL&for=us:*>`_
* ``yibszfi`` (optional)
   - years in business
   - `options for CSA yibszfi input <https://api.census.gov/data/2014/ase/csa?get=YIBSZFI,YIBSZFI_TTL&for=us:*>`_
* ``eth_group`` (optional)
   - gender, ethnicity, race, and veteran status
   - `options for CSA eth_group input <https://api.census.gov/data/2014/ase/csa?get=ETH_GROUP,ETH_GROUP_TTL&for=us:*>`_
* ``race_group`` (optional)
   - race code
   - `options for CSA race_group input <https://api.census.gov/data/2014/ase/csa?get=RACE_GROUP,RACE_GROUP_TTL&for=us:*>`_

Other Documentation (CSA)
^^^^^^^^^^^^^^^^^^^^^^^^^^
* `General information about the ASE database <https://www.census.gov/data/developers/data-sets/ase.html>`_
* `CSA API call examples and supported geographies <https://api.census.gov/data/2014/ase/csa/examples.html>`_
* `List of available CSA metrics/variables <https://api.census.gov/data/2014/ase/csa/variables.html>`_
* `FIPS State Codes <https://www.mcc.co.mercer.pa.us/dps/state_fips_code_listing.htm>`_

Overview (CSCB)
^^^^^^^^^^^^^^^^^^^^^
Provides data for employer firms by sector, gender, ethnicity, race, veteran status, and years in business for the U.S., states, and fifty most populous MSAs, including detailed business characteristics.

Parameters (CSCB)
^^^^^^^^^^^^^^^^^^^^^
* ``metric`` (**required**)
   - specify metric to pull
   - `full CSCB variables list <https://api.census.gov/data/2014/ase/cscb/variables.html>`_
* ``code`` (**conditionally required**)
   - specify state or metro FIPS code
   - only required if geographic level != us
   - `FIPS state codes <https://www.mcc.co.mercer.pa.us/dps/state_fips_code_listing.htm>`_
* ``acqbuscap`` (optional)
   - amount of capital used to start or acquire the business
   - `options for CSCB acqbuscap input <https://api.census.gov/data/2014/ase/cscb?get=ACQBUSCAP,ACQBUSCAP_TTL&for=us:*>`_
* ``asecb`` (optional)
   - gender, race, ethnicity, and veteran status code
   - `options for CSCB asecb input <https://api.census.gov/data/2014/ase/cscb?get=ASECB,ASECB_TTL&for=us:*>`_
* ``avoidfinan`` (optional)
   - reasons for avoiding additional financing
   - `options for CSCB avoidfinan input <https://api.census.gov/data/2014/ase/cscb?get=AVOIDFINAN,AVOIDFINAN_TTL&for=us:*>`_
* ``benefits`` (optional)
   - employee benefits paid totally or partly by the business
   - `options for CSCB benefits input <https://api.census.gov/data/2014/ase/cscb?get=BENEFITS,BENEFITS_TTL&for=us:*>`_
* ``busact`` (optional)
   - business activity characteristics
   - `options for CSCB busact input <https://api.census.gov/data/2014/ase/cscb?get=BUSACT,BUSACT_TTL&for=us:*>`_
* ``busaspir`` (optional)
   - owner's business aspirations
   - `options for CSCB busaspir input <https://api.census.gov/data/2014/ase/cscb?get=BUSASPIR,BUSASPIR_TTL&for=us:*>`_
* ``busoutus`` (optional)
   - operations outside of the US
   - `options for CSCB busoutus input <https://api.census.gov/data/2014/ase/cscb?get=BUSOUTUS,BUSOUTUS_TTL&for=us:*>`_
* ``ceaseops`` (optional)
   - whether business is currently operating or if not, reason for ceasing operations
   - `options for CSCB ceaseops input <https://api.census.gov/data/2014/ase/cscb?get=CEASEOPS,CEASEOPS_TTL&for=us:*>`_
* ``cust`` (optional)
   - customers accounting for 10% or more of total sales of goods/services
   - `options for CSCB cust input <https://api.census.gov/data/2014/ase/cscb?get=CUST,CUST_TTL&for=us:*>`_
* ``custlocpct`` (optional)
   - geographic location of business customers/clients
   - `options for CSCB custlocpct input <https://api.census.gov/data/2014/ase/cscb?get=CUSTLOCPCT,CUSTLOCPCT_TTL&for=us:*>`_
* ``famown`` (optional)
   - family owned business codes
   - `options for CSCB famown input <https://api.census.gov/data/2014/ase/cscb?get=FAMOWN,FAMOWN_TTL&for=us:*>`_
* ``fundsrc`` (optional)
   - funding sources and total amount of funding
   - `options for CSCB fundsrc input <https://api.census.gov/data/2014/ase/cscb?get=FUNDSRC,FUNDSRC_TTL&for=us:*>`_
* ``innovimp`` (optional)
   - business product/process innovations/improvements in the past three years
   - `options for CSCB innovimp input <https://api.census.gov/data/2014/ase/cscb?get=INNOVIMP,INNOVIMP_TTL&for=us:*>`_
* ``intelctprop`` (optional)
   - owned intellectual property
   - `options for CSCB intelctprop input <https://api.census.gov/data/2014/ase/cscb?get=INTELCTPROP,INTELCTPROP_TTL&for=us:*>`_
* ``lang`` (optional)
   - languages used to conduct transactions with customers
   - `options for CSCB lang input <https://api.census.gov/data/2014/ase/cscb?get=LANG,LANG_TTL&for=us:*>`_
* ``naics2012`` (optional)
   - 2012 NAICS codes
   - `options for CSCB naics2012 input <https://api.census.gov/data/2014/ase/cscb?get=NAICS2012,NAICS2012_TTL&for=us:*>`_
* ``negprofit`` (optional)
   - negative impacts on business profitability
   - `options for CSCB negprofit input <https://api.census.gov/data/2014/ase/cscb?get=NEGPROFIT,NEGPROFIT_TTL&for=us:*>`_
* ``newfundrel`` (optional)
   - new funding relationships
   - `options for CSCB newfundrel input <https://api.census.gov/data/2014/ase/cscb?get=NEWFUNDREL,NEWFUNDREL_TTL&for=us:*>`_
* ``opfran`` (optional)
   - year business was established
   - `options for CSCB opfran input <https://api.census.gov/data/2014/ase/cscb?get=OPFRAN,OPFRAN_TTL&for=us:*>`_
* ``outsrcus`` (optional)
   - business functions or services outsourced to a location outside the US
   - `options for CSCB outsrcus input <https://api.census.gov/data/2014/ase/cscb?get=OUTSRCUS,OUTSRCUS_TTL&for=us:*>`_
* ``ownrnum`` (optional)
   - number of owners in the business code
   - `options for CSCB ownrnum input <https://api.census.gov/data/2014/ase/cscb?get=OWNRNUM,OWNRNUM_TTL&for=us:*>`_
* ``pecommrc`` (optional)
   - e-commerce sales as a % of total sales
   - `options for CSCB pecommrc input <https://api.census.gov/data/2014/ase/cscb?get=PECOMMRC,PECOMMRC_TTL&for=us:*>`_
* ``pexport`` (optional)
   - exports sales as a % of total sales
   - `options for CSCB pexport input <https://api.census.gov/data/2014/ase/cscb?get=PEXPORT,PEXPORT_TTL&for=us:*>`_
* ``profit`` (optional)
   - profitability of the business
   - `options for CSCB profit input <https://api.census.gov/data/2014/ase/cscb?get=PROFIT,PROFIT_TTL&for=us:*>`_
* ``rdpuramt`` (optional)
   - amount used to purchase R&D activities
   - `options for CSCB rdpuramt input <https://api.census.gov/data/2014/ase/cscb?get=RDPURAMT,RDPURAMT_TTL&for=us:*>`_
* ``rdtotalcst`` (optional)
   - total cost of R&D activities
   - `options for CSCB rdtotalcst input <https://api.census.gov/data/2014/ase/cscb?get=RDTOTALCST,RDTOTALCST_TTL&for=us:*>`_
* ``rdworkers`` (optional)
   - workers that did the R&D activities
   - `options for CSCB rdworkers input <https://api.census.gov/data/2014/ase/cscb?get=RDWORKERS,RDWORKERS_TTL&for=us:*>`_
* ``spouses`` (optional)
   - spouses jointly owned and operated business codes
   - `options for CSCB spouses input <https://api.census.gov/data/2014/ase/cscb?get=SPOUSES,SPOUSES_TTL&for=us:*>`_
* ``strtsrce`` (optional)
   - sources of capital used to start or acquire the business
   - `options for CSCB strtsrce input <https://api.census.gov/data/2014/ase/cscb?get=STRTSRCE,STRTSRCE_TTL&for=us:*>`_
* ``website`` (optional)
   - business website codes
   - `options for CSCB website input <https://api.census.gov/data/2014/ase/cscb?get=WEBSITE,WEBSITE_TTL&for=us:*>`_
* ``workers`` (optional)
   - types of workers used codes
   - `options for CSCB workers input <https://api.census.gov/data/2014/ase/cscb?get=WORKERS,WORKERS_TTL&for=us:*>`_
* ``yibszfi`` (optional)
   - years in business
   - `options for CSCB yibszfi input <https://api.census.gov/data/2014/ase/cscb?get=YIBSZFI,YIBSZFI_TTL&for=us:*>`_
* ``yrestbus`` (optional)
   - year business was originally established
   - `options for CSCB yrestbus input <https://api.census.gov/data/2014/ase/cscb?get=YRESTBUS,YRESTBUS_TTL&for=us:*>`_

Other Documentation (CSCB)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* `General information about the ASE database <https://www.census.gov/data/developers/data-sets/ase.html>`_
* `CSCB API call examples and supported geographies <https://api.census.gov/data/2014/ase/cscb/examples.html>`_
* `List of available CSCB metrics/variables <https://api.census.gov/data/2014/ase/cscb/variables.html>`_
* `FIPS State Codes <https://www.mcc.co.mercer.pa.us/dps/state_fips_code_listing.htm>`_

Overview (CSCBO)
^^^^^^^^^^^^^^^^^^^^^
Provides data for owners of respondent employer firms by sector, gender, ethnicity, race, veteran status, and years in business for the U.S., states, and top fifty most populous MSAs, including detailed owner characteristics.

Parameters (CSCBO)
^^^^^^^^^^^^^^^^^^^^^
* ``metric`` (**required**)
   - specify metric to pull
   - only option for CSBO is ``ownpdemp`` and variations on it
   - `full CSCBO variables list <https://api.census.gov/data/2014/ase/cscbo/variables.html>`_
* ``code`` (**conditionally required**)
   - specify state or metro FIPS code
   - only required if geographic level != us
   - `FIPS state codes <https://www.mcc.co.mercer.pa.us/dps/state_fips_code_listing.htm>`_
* ``acqbus`` (optional)
   - how owner initially acquired business
   - `options for CSCBO acqbus input <https://api.census.gov/data/2014/ase/cscbo?get=ACQBUS,ACQBUS_TTL,OWNPDEMP&for=us:*>`_
* ``asecbo`` (optional)
   - gender, ethnicity, race, and veteran status code
   - `options for CSCBO asecbo input <https://api.census.gov/data/2014/ase/cscbo?get=ASECBO,ASECBO_TTL,OWNPDEMP&for=us:*>`_
* ``educ`` (optional)
   - highest level of education before establishing business
   - `options for CSCBO educ input <https://api.census.gov/data/2014/ase/cscbo?get=EDUC,EDUC_TTL,OWNPDEMP&for=us:*>`_
* ``hrswrkd`` (optional)
   - average hours spent per week managing or working in business
   - `options for CSCBO hrswrkd input <https://api.census.gov/data/2014/ase/cscbo?get=HRSWRKD,HRSWRKD_TTL,OWNPDEMP&for=us:*>`_
* ``naics2012`` (optional)
   - 2012 naics codes
   - `options for CSCBO naics2012 input <https://api.census.gov/data/2014/ase/cscbo?get=NAICS2012,NAICS2012_TTL,ACQBUS,OWNPDEMP&for=us:*>`_
* ``ownrage`` (optional)
   - owner's age
   - `options for CSCBO ownrage input <https://api.census.gov/data/2014/ase/cscbo?get=OWNRAGE,OWNRAGE_TTL,OWNPDEMP&for=us:*>`_
* ``pfnct`` (optional)
   - primary functions in the business
   - `options for CSCBO pfnct input <https://api.census.gov/data/2014/ase/cscbo?get=PFNCT,PFNCT_TTL,OWNPDEMP&for=us:*>`_
* ``priorbus`` (optional)
   - whether they owned another business prior to establishing current business
   - `options for CSCBO priorbus input <https://api.census.gov/data/2014/ase/cscbo?get=PRIORBUS,PRIORBUS_TTL,OWNPDEMP&for=us:*>`_
* ``prminc`` (optional)
   - primary source of personal income
   - `options for CSCBO prminc input <https://api.census.gov/data/2014/ase/cscbo?get=PRMINC,PRMINC_TTL,OWNPDEMP&for=us:*>`_
* ``usborncit`` (optional)
   - whether they are a US born citizen
   - `options for CSCBO usborncit input <https://api.census.gov/data/2014/ase/cscbo?get=USBORNCIT,USBORNCIT_TTL,OWNPDEMP&for=us:*>`_
* ``yracqbus`` (optional)
   - year when business was acquired
   - `options for CSCBO yracqbus input <https://api.census.gov/data/2014/ase/cscbo?get=YRACQBUS,YRACQBUS_TTL,OWNPDEMP&for=us:*>`_

Other Documentation (CSCBO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* `General information about the ASE database <https://www.census.gov/data/developers/data-sets/ase.html>`_
* `CSCBO API call examples and supported geographies <https://api.census.gov/data/2014/ase/cscbo/examples.html>`_
* `List of available CSCBO metrics/variables <https://api.census.gov/data/2014/ase/cscbo/variables.html>`_
* `FIPS State Codes <https://www.mcc.co.mercer.pa.us/dps/state_fips_code_listing.htm>`_

Goals
===============
Broadly speaking, my goal is to cover all the business-focused datasets before moving to the purely demographic data. The main motivation behind that is personal, since I'm deriving personal value from developing this wrapper. That being said -- if there is significant interest in exposing a specific dataset, then I'm more than happy to entertain that as well. Please feel free to send any requests to dnrkaseff360@gmail.com.

**Roadmap**:

* Annual Survey of Entrepreneurs (March 2018) [**DONE**]
* County Business Patterns and Nonemployer Statistics (April 2018)
* Economic Census (May 2018)
* Economic Indicators (June 2018)

Changelog
===============
* 0.0.1: initial beta release
* 0.0.2: hot fix to allow imports of specific database wrappers instead of having to import the entire package
* 1.0.0: **go live!** added support for ASE and implemented minor code changes to make calls more efficient from a resource perspective

License
===============
**MIT License**

Copyright (c) 2018 DnrkasEFF

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
