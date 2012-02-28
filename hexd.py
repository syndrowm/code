#!/usr/bin/env python
import sys

if sys.stdout.isatty():
    GREEN = '\x1b[32m'
    RESET = '\x1b[0m'
else:
    GREEN = ''
    RESET = ''

def isprint(c):
    return ord(c) >= 32 and ord(c) <=126

def dot_or_ascii(chr):
    if isprint(chr):
        return chr
    else:
        return '.'

def chck(o, n):
    if o == n:
        return (True, n)
    else:
        return (False, n)

def hexdiff(orig, new):
    diff = map(chck, orig, new)

    d = ''
    for i in xrange(0, len(diff), 16):
        d += '%08x  ' % i

        count = 0
        rep = ''
        n = ''
        for j in diff[i:i+16]:
            if j[0]:
                n += '%02x' % ord(j[1])
                rep += dot_or_ascii(j[1])
            else:
                n += '%s%02x%s' % (GREEN, ord(j[1]), RESET)
                rep += '%s%c%s' % (GREEN, dot_or_ascii(j[1]), RESET)
            n += ' '
            count += 1
            if not count % 8:
                n += ' '

        n += ' ' * (50 - len(n))                                                                                                           
        d += n
        d += '|'
        d += rep + '|'
        d += '\n'
    d += '%08x' % (i + 16)
    return d

if __name__ == '__main__':
    
    try:
        file1 = open(sys.argv[1]).read()
        file2 = open(sys.argv[2]).read()
    except:
        print "Usage: %s file1 file2" % sys.argv[0]
        exit(1)

    print hexdiff(file1, file2)
