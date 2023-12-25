#!/usr/bin/python3
import sys
import re


class Interval(object):

    def __init__(self, line):
        v = re.split(r'\s+', line)
        self.destination, self.source, self.length = [int(x) for x in v]

    def map(self, s):
        if s < self.source or s > (self.source + self.length):
            return s
        return self.destination + (s - self.source)


def process_seed(data):
    _, s = re.split(r':\s+', data)
    return [int(x) for x in re.split(r'\s+', s)]


def process_section(lines, start):
    intervals = []

    title = lines[start]
    i = start + 1
    
    while i < len(lines) and lines[i]:
        intervals.append(Interval(lines[i]))
        i += 1
    
    return i, intervals


def process_data(data):
    lines = [x.rstrip() for x in data]
    seeds = process_seed(lines[0])

    i = 2
    while i < len(lines):
        i, intervals = process_section(lines, i)
        i += 1
        new_seeds = []
        for s in seeds:
            m = [x.map(s) for x in intervals]
            v = s
            for c in m:
                if c != s:
                    v = c
            new_seeds.append(v)
        seeds = new_seeds

    return min(seeds)


if __name__ == '__main__':
    res = process_data(open(sys.argv[1]))
    print('results: %d' % res)
