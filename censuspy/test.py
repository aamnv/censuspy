import census


code = '04'
state = census.bds('61452b999f5349ac5ac1951f55506efb2f0ad72d', 'state', 2014)
emp = state.emp(code)
estabs = state.estabs(code)
firms = state.firms(code)
job_creation = state.job_creation(code)
job_destruction = state.job_destruction(code)
net_job_creation = state.net_job_creation(code)


print("Arizona:")
print('Total employees: ' + str(emp))
print('Total establishments: ' + str(estabs))
print('Total firms: ' + str(firms))
print('Total jobs created: ' + str(job_creation))
print('Total jobs destroyed: ' + str(job_destruction))
print('Net jobs created/destroyed: ' + str(net_job_creation))
