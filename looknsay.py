#!/usr/bin/env python
#Look-and-say sequence
from itertools import groupby

def looknsay(value, length):
    """
    Generates an iterable object of the look-and-say sequence with the first
    value, and with a given length.
    """
    yield value
    for i in xrange(length):
        value = reduce(lambda s, (a, b): s + str(len(list(b))) + a,
                        groupby(value), '')
        yield value

if __name__ == "__main__":
    # Python Challenge 10 - find the length of the 31st item of this
    print len(list(looknsay('1',31))[30])

