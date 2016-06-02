import urllib.request


webpage = urllib.request.urlopen('http://www.badu.com')
w = webpage.read()
s = w.decode('utf8')
webpage.close()
print(s)
