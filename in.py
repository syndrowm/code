#!/usr/bin/env python
import os
import select
import socket
import sys

# Interact with TCP sockets with color =)

colors = 'RED GREEN YELLOW BLUE MAGENTA CYAN WHITE'.split()

for i,j in enumerate(colors):
    locals()[j] = '\x1b[3%sm' % (i+1)

def puts(msg, color=''):
    reset = '\x1b[0m'
    if not os.isatty(sys.stdin.fileno()):
        color = ''
        reset = ''
    sys.stdout.write("%s%s%s" % (color, msg, reset))
    sys.stdout.flush()

def read_until(s, char):
    result = ''
    while True:
        r,w,x = select.select([s], [], [], .1)
        if s in r:
            result += s.recv(1)
            if result.endswith(char):
                break
    return result

def interact(s):
    while True:
        r,w,x = select.select([s, sys.stdin], [], [], .1)
        if s in r:
            inp = s.recv(1024)
            if inp == '':
                break
            else:
                puts(inp, RED)
        if sys.stdin in r:
            s.sendall(sys.stdin.readline())

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print "Usage: %s HOST PORT" % sys.argv[0]
        exit(1)

    s = socket.create_connection((sys.argv[1], int(sys.argv[2])))
    interact(s)
