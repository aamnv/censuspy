============
CensusPy
============
The goal of CensusPy is to expose the vast amount of data the government collects on US citizens to the broader programming community.

Written as a wrapper around existing census APIs, v0.1 of CensusPy currently supports the `Business Dynamics Statistics <https://www.census.gov/data/developers/data-sets/business-dynamics.html>`_ database. But, the end goal will be to support all databases provided by the Census Bureau.

Installation
===============
CensusPy is supported on PyPi, so installation is as simple as::

  pip install censuspy

Business Dynamics Statistics (BDS)
===================================

Quickstart
^^^^^^^^^^^^^^^^^^^^^
Initialize the BDS object using your API key & geographic level of query::

  bds = census.bds(api_key=[YOUR_API_KEY_HERE], geo='state')

Pull total employment numbers for Massachusetts (FIPS code 25) in 2014::

  ma_emp = bds.get(metric='emp', code=25, time=2014)
  print(ma_emp)

Reference Materials
^^^^^^^^^^^^^^^^^^^
* General information about the BDS database: http://bit.ly/2BHqjWd
* Examples and support geographies: http://bit.ly/2CBkeaN
* List of available metrics/variables: http://bit.ly/2GvGDIE
* FIPS State Codes: http://bit.ly/2EUgw1c

Goals
===============
Broadly speaking, my goal is to cover all the business-focused datasets before moving to the purely demographic data. The main motivation behind that is personal, since I'm deriving personal value from developing this wrapper. That being said -- if there is significant interest in exposing a specific dataset, then I'm more than happy to entertain that as well. Please feel free to send any requests to dnrkaseff360@gmail.com.

**Roadmap**:

* Annual Survey of Entrepreneurs (March 2018)
* County Business Patterns and Nonemployer Statistics (April 2018)
* Economic Census (May 2018)
* Economic Indicators (June 2018)

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
