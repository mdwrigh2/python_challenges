#!/usr/bin/env python
from string import maketrans
from sys import stdin

intab = str(raw_input("From: \n"))
outtab = str(raw_input("To: \n"))
string = str(raw_input("String: \n"))
print "Translation: \n"+string.translate(maketrans(intab,outtab))