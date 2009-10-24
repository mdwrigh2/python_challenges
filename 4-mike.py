#!/usr/env python
import re
import urllib2
site = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=46059').read()
number_snatcher = re.compile('is ([0-9]+)')
numbers = number_snatcher.findall(site)
print numbers
while(numbers):
    site = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+numbers[0]).read()
    number_snatcher = re.compile('is ([0-9]+)')
    numbers = number_snatcher.findall(site)
    print numbers