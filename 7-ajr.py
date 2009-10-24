#!/usr/bin/env python
#starts at 0,43; first is 5 wide; else are 7 wide
import re
from PIL import Image
im = Image.open('oxygen.png')
size = im.getbbox()
pix = im.load()
lastcolor = None
s = ''
for i in range(0,size[2],7):
    color = pix[i, 43]
    if color[0] == color[1] and color[1] == color[2]:
        s += chr(color[0])
    lastcolor = color
print ''.join(map(chr,eval(re.findall('(\[[^\]]*\])',s)[-1])))
