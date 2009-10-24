#!/usr/bin/env python
import re, zipfile
z = zipfile.ZipFile('channel.zip')
num = '90052.txt'
s = ''
while True:
    print 'opening', num
    a = z.open(num)
    num = str(re.findall('\d+',a.read())[-1])+'.txt'
    s += z.getinfo(num).comment
    a.close()
    print s
