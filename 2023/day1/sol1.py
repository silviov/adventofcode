#!/usr/bin/python3
import sys

def process_data(lines):
    res = 0
    for l in lines:
        first = 0
        for c in l:
            if c.isnumeric():
                first = int(c)
                break
        second = 0
        for c in reversed(l):
            if c.isnumeric():
                second = int(c)
                break
        # print ("adding %d\n" % (first * 10 + second))
        res += (first*10 + second)
    return res

def process_file(filename):
    f = open(filename)
    n = process_data(f)
    print ("result: %d\n" % n)

if __name__ == '__main__':
    process_file(sys.argv[1])
