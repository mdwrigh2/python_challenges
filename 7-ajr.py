#!/usr/bin/env python
#starts at 0,43; first is 5 wide; else are 7 wide, sampling every 7
import re, PIL.Image
im = PIL.Image.open('oxygen.png')
print ''.join(map(chr,eval(re.findall('(\[[^\]]*\])', ''.join([chr(im.getpixel((i, 43))[0]) for i in range(0,im.getbbox()[2],7) if im.getpixel((i, 43))[0] == im.getpixel((i, 43))[1] == im.getpixel((i, 43))[2]]))[-1])))
