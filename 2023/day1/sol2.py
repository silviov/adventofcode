#!/usr/bin/python3
import sys

NAMES = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'zero': 0,
        }

def check_num(s):
    if s[0].isnumeric():
        return int(s[0])
    for k in NAMES.keys():
        if s.startswith(k):
            return NAMES[k]
    return -1

def process_data(lines):
    res = 0
    for l in lines:
        values = []
        for n in range(len(l)):
            v = check_num(l[n:])
            if v >= 0:
                values.append(v)
        if not values:
            continue
        v = values[0] * 10 + values[-1]
        print ("adding %d\n" % v)
        res += v
    return res

def process_file(filename):
    f = open(filename)
    n = process_data(f)
    print ("result: %d\n" % n)

if __name__ == '__main__':
    process_file(sys.argv[1])
