#!/usr/bin/python3
import sys
import re

def process_line(line):
    _, data = re.split(r':\s+', line)
    return [int(x) for x in re.split(r'\s+', data)]


def count_wins(time, record):
    return sum(1 for t in range(time) if t * (time -t) > record)


def process_data(data):
    times = process_line(data[0])
    records = process_line(data[1])

    res = 1
    for t, r in zip(times, records):
        res *= count_wins(t, r)
    return res


if __name__ == '__main__':
    res = process_data(list(x.rstrip('\n') for x in open(sys.argv[1])))
    print('results: %d' % res)
