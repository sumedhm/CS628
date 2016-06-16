import urllib
import urllib2
import requests
url = 'https://172.27.20.32:8443/login.php'
values = {'username': 'sumedh',
          'password': 'CXbXPGbNfXNvBEL'}

session = requests.session()
r = session.post(url, data=values, verify=False)
#print r.content

url = 'https://172.27.20.32:8443/chal10.php'
values = {'username' : 'admin'}
r = session.post(url, data=values, verify = False)
print r.headers
print r.cookies
#print r.content.find("This user exists")



