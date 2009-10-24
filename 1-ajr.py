#!/usr/bin/env python
from sys import stdin as s
from string import maketrans as m
i = s.read();o = s.read()
print s.read().translate(m(i,o))
