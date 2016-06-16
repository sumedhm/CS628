import urllib
import urllib2
import requests
url = 'https://172.27.20.32:8443/login.php'
values = {'username': 'sumedh',
          'password': 'CXbXPGbNfXNvBEL'}

session = requests.session()
r = session.post(url, data=values, verify=False)
#print r.content

url = 'https://172.27.20.32:8443/chal8.php'
cookie = {'logged_in' : '1'}
header = {'referer': "example.com",
	  'User-Agent': "CS628"
	}
r = session.post(url, cookies=cookie, headers=header, verify = False)
print r.headers
print r.content



