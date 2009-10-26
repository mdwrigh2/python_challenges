#!/usr/bin/env python
from sys import stdin as s
i = s.read();o = s.read()
print s.read().translate(string.maketrans(i,o))
