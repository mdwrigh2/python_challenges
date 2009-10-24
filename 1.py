#!/bin/python
# Translate the block of text:

#g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. 

# Using the translation key of k->m o->q and e->g.
import string
initial = str(raw_input("From: \n"))
final = str(raw_input("To: \n"))

quote = raw_input("Quote: \n")
print quote.translate(string.maketrans(initial,final))
print '\n\n\n\n ocr is the answer'
