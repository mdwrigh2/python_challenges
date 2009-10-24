#!/usr/bin/env python
#starts at 0,43; first is 5 wide; else are 7 wide, sampling every 7
import PIL.Image;print ''.join(map(chr,eval(PIL.Image.open('oxygen.png').tostring()[108188:110620:28][42:])))
