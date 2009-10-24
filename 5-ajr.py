#!/usr/bin/env python
import pickle
a = pickle.load(open('banner.p'))
s = ''
for line in a:
    for bit in line: s += bit[0]*bit[1]
    s += '\n'
print s
