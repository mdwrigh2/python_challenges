#!/usr/bin/env python
import re, zipfile
z = zipfile.ZipFile('channel.zip')
num = '90052.txt'
s = ''
while True:
  try:
    a = z.open(num)
    num = str(re.findall('\d+',a.read())[-1])+'.txt'
    s += z.getinfo(num).comment
  except:
    print s
    break
