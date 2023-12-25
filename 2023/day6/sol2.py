#!/usr/bin/python3
import sys
import re
import math

def process_line(line):
    _, data = re.split(r':\s+', line)
    return int(re.sub(r'\s+', '', data))


def count_wins(time, record):
    delta = math.sqrt(time*time - 4 * record)
    x1 = math.ceil((time + delta) / 2)
    x2 = math.floor((time - delta) / 2)
    print(time, record, delta, x1, x2)
    return time - int(x2 + (time - x1)) - 1

def process_data(data):
    t = process_line(data[0])
    r = process_line(data[1])
    return count_wins(t, r)


if __name__ == '__main__':
    res = process_data(list(x.rstrip('\n') for x in open(sys.argv[1])))
    print('results: %d' % res)
