#!/usr/bin/env python
#Look-and-say sequence

a = ['1']
for i in xrange(1,31):
    s = ''
    b = 0
    while b < len(a[i-1]):
        c = a[i-1][b]
        n = 1
        while b+n < len(a[i-1]) and c == a[i-1][b+n]:
            n += 1
        s += str(n)+c
        b += n
    a.append(s)

print len(a[30])
