#!/bin/python
#Apparently they mean pickle... but what from there?
import pickle
quote = """"""
file = open('5_banner.p', 'rb')
struct = pickle.load(file)
banner = ''
level0 = ''
level1 = 0
for part in struct:
	for pair in part:
		if pair[0] == ' ':
			banner += (' ' * pair[1])
		else:
			banner += ('#' * pair[1])
	banner += '\n'
print banner
