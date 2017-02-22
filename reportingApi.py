#!/usr/bin python

from __future__ import print_function
import requests
print('\nStarting Reporting API Pull')
#file set up
file = 'apiResults.txt'
output = open(file,'w')
#auth step
s = requests.session()
with open('secrets.txt') as f:
  credentials = [x.strip().split(':') for x in f.readlines()]
for username,password in credentials:
	data = {"j_username":username,"j_password":password}
	authreq = s.post('https://reportingAPI.com/reportingservice/j_spring_security_check', data=data)
if authreq.status_code == 200:
    print ('\nStatus:200 - authorized')
elif authreq.status_code == 302:
    print ('\nStatus:302 - temporarily redirected')
else:
    print ('\nError - login again')
#request report step
apirequest = raw_input('\nEnter request URL: ')
req = '{0}'.format(apirequest)
apiget = s.get(req)
results = apiget.text
print (results, file=output)
print ('\ndone')
