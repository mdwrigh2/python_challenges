#!/usr/bin/env python
import re,sys 
print ''.join(re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]').findall(sys.stdin.read()))
