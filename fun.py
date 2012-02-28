#!/usr/bin/env python

# slowly converting asciifun.pl to python
# syndrowm - 6/14/2007
# 9/22/2011 - I suck at python less now

import struct
import sys
# ascii escape colors
GREEN="[032;40m"
RESET="[0;0;40m"

def usage():
    print 'Usage: %s string or hex' % sys.argv[0]
    sys.exit(0)

def join(format, xlist, sep):
    return sep.join([format % ord(i) for i in xlist])

if __name__ == '__main__':

    if len(sys.argv) - 1 < 1:
        usage()

    if sys.argv[1].startswith('0x'): 
        if len(sys.argv[1]) == 10 or len(sys.argv[1]) == 9:
            line = struct.pack("I", int(sys.argv[1], 16))
        else:
            line = sys.argv[1][2:].decode('hex')
    else:
        line = sys.argv[1]

    print GREEN + "ascii:" + RESET, line
    print GREEN + "  hex:" + RESET, join('%02x', line, ' ')
    print GREEN + "  dec:" + RESET, join('%02d', line, ' ')
    print GREEN + "  oct:" + RESET, join('%o', line, ' ')
    print GREEN + "bytes:" + RESET, join('\\x%02x', line, '')
