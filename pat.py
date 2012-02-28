#!/usr/bin/python
import getopt
import string
import struct
import sys

def converge_sets(sets, idx, offsets, length):

    buf = sets[idx][offsets[idx]]

    try:
        buf += converge_sets(sets, idx + 1, offsets, length)
    except IndexError:
        while idx >= 0:
            offsets[idx] = ((offsets[idx]) + 1) % (len(sets[idx]))
            if offsets[idx] == 0:
                idx -= 1
            else:
                break
        if idx < 0:
            raise "Error"

    return buf

def pattern_create(length, sets = [ string.uppercase, string.lowercase, string.digits]):
    buf = ''
    idx = 0
    offsets = [0] * len(sets)

    while len(buf) < length:
        try:
            buf += converge_sets(sets, 0, offsets, length)
        except Exception, e:
            break

    if len(buf) < length:
        buf = buf * (length / len(buf))

    return buf[0:length]

def usage(code):
    print "Usage: %s [-h --help] [-c --create=size] [-f --find=size]" % sys.argv[0]
    print " -c --create=size\t\tsize of pattern to create"
    print " -f --find=0x41414141\t\thex value from register"
    print " -h --help\t\tdisplay this message"
    sys.exit(code)

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:f:", ["help",
                                                       "create=",
                                                       "find=" ])
    except getopt.GetoptError:
        usage(1)

    f = 0
    pat = 0
    for opt,arg in opts:
        #print opt, arg
        if opt in ("-h", "--help"):
            usage(0)
        elif opt in ("-c", "--create"):
            pat = pattern_create(int(arg))
        elif opt in ("-f", "--find"):
            try:
                f = struct.pack('I', int(arg, 16))
            except:
                usage(2)

    if f and pat:
        print pat.find(f)
    elif f and not pat:
        pat = pattern_create(8192)
        print pat.find(f)
    elif pat:
        print pat
    else:
        usage(3)
