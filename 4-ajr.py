#!/usr/bin/env python
import urllib2,re
base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num = '46059' #'12345'
while True:
    print 'opening ',num
    a = urllib2.urlopen(base+num)
    num = str(re.findall('\d+',a.read())[-1])
    a.close()
