import pickle, pprint, sys
pk1_file = open('banner.p', 'rb')
data1 = pickle.load(pk1_file)
banner = ''
for part in struct:
	for pair in part:
        banner += pair[0]*pair[1]
	banner += '\n'
print banner