import census

bds = census.bds(api_key=YOUR_API_KEY_HERE, geo='state')
ma_emp = bds.get(metric='emp', code=25, time=2014)

print(ma_emp)