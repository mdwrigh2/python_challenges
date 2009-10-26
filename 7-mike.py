#!/usr/bin/env python
#starts at 0,43; first is 5 wide; else are 7 wide, sampling every 7
import PIL.Image as image

img = image.open("oxygen.png")

width = img.getbbox()[2]


a = ''
a += chr(img.getpixel((0, 43))[0])
for i in range(5,width,7):
    a += chr(img.getpixel((i, 43))[0])
    
print a

b = ''
sol_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in sol_list:
    b +=  chr(i)

print b