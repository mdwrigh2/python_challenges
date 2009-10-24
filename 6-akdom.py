#!/bin/python
#hockey.html is the answer!
#Zip file found at channel.zip.
#Jump through files (instead of urls) like problem #4 'til it says "Collect the Comments".
#By "comments" it means comments on the files in the zip archive.
#Each file has a single character comment, and when you display them in the order jumped through they
#	banner out HOCKEY in ascii art.
import re, os, zipfile
grab = open('6_channel/90052.txt').read()
digits = re.compile('[0-9]+')

used_files = {'90052':''}
i = 0
while i < 908:
	next = digits.findall(grab)
	next = next[len(next) - 1]
	grab = open('6_channel/' + next + '.txt').read()
	used_files[i] = grab
	i += 1

all_files = [num[0] for num in (digits.findall(line.strip()) for line in os.popen('ls 6_channel', 'r')) if len(num) > 0] # and num != ['6']]
unused_files = [key for key in all_files if key not in used_files]

archive = zipfile.ZipFile('6_channel/6_channel.zip')
print ''.join([archive.getinfo(digits.findall(file)[0] + '.txt').comment for key,file in used_files.iteritems() if len(digits.findall(file)) > 0])
