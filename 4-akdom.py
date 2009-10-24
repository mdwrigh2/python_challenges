#!/bin/python
#Grab page from url of http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345 and remove all but numbers, plug into place of 12345, lather rinse repeat, until the page loads cleanly.
#Don't forget to divide by two when it asks...
#peak.html is the answer!
import urllib, re
grab = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=46059').read()
digits = re.compile('[0-9]+')

i = 400
while i:
	next = digits.findall(grab)
	next = next[len(next) - 1]
	print next
	grab = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + next).read()
	print grab
	i -= 1
