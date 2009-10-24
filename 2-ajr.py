#!/usr/bin/env python
from sys import stdin as s
b = s.read()
i = dict([(chr(i),0) for i in range(256)])
for c in b: i[c] += 1
for l in sorted(i.iteritems(), key=lambda (k,v): (v,k)): print l
