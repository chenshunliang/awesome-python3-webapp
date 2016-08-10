import re
import time

# Create your tests here.
import os
import csv
import urllib2
import datetime

print(os.path.basename('/etc/a.txt'))

r = re.compile(r'\d+', re.I)

result = r.search('123abd345sdq332e')
if result:
    print(result.group())
else:
    print('None')

print(os.name)
print(os.getcwd())
# print(os.linesep, re.search('aaa'))
print(os.path.split('/etc/a.txt'))
print(time.ctime())
print(time.time())
# print(csv.)
# u = urllib2.urlopen('http://www.baidu.com')
# print(u.read())
# print(dir(csv))
now = datetime.datetime.now()
past = datetime.datetime(2010, 11, 12, 13, 14, 15, 16)
print(dir(datetime.datetime.now()))
print(now.timetuple())
print((now - past).days)

if __name__ == '__main__':
    print('ok')
    r = re.search(r'(\d+)', 'asa123sa')
    print(r)
