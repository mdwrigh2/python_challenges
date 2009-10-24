#!/usr/bin/env python
#starts at 0,43; first is 5 wide; else are 7 wide, sampling every 7
import re, PIL.Image
im = PIL.Image.open('oxygen.png')
pix = im.load()
s = ''
for i in range(0,im.getbbox()[2],7):
    color = pix[i, 43]
    if color[0] == color[1] and color[1] == color[2]:
        s += chr(color[0])
print ''.join(map(chr,eval(re.findall('(\[[^\]]*\])',s)[-1])))

print ''.join(map(chr,eval(re.findall('(\[[^\]]*\])', ''.join([chr(pix[i, 43][0]) for i in range(0,im.getbbox()[2],7 if pix[i, 43][0] == pix[i, 43][1] == pix[i, 43][2]]))[-1])))
