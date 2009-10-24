#!/usr/bin/env python
import re

blob = str(raw_input())
big_brothers = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
print big_brothers.findall(blob)