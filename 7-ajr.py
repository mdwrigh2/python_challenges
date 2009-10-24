#!/usr/bin/env python
#starts at 0,43; first is 5 wide; else are 7 wide, sampling every 7
import re, PIL.Image;im=PIL.Image.open('oxygen.png');p=lambda l,k: im.getpixel((l,43))[k];j= lambda m:''.join(m);print j(map(chr,eval(re.findall('(\[[^\]]*\])',j([chr(p(i,0)) for i in range(0,im.getbbox()[2],7) if p(i,0)==p(i,1)==p(i,2)]))[-1])))
