#!/usr/bin/python3
import sys
import re

class Interval(object):

    def __init__(self, x):
        self.start = x[0]
        self.length = x[1]

    @property
    def end(self):
        return self.start + self.length

    def __repr__(self):
        return '(%d, %d)' % (self.start, self.end)

    def map(self, intervals):
        res = []
        start = self.start
        end = self.end

        for i in intervals:
            # skip over the mappings that are too early
            if start >= i.end:
                continue

            # skip over the mapping that are too late
            if end < i.start:
                continue

            if start < i.start:
                res.append((start, i.start))
                start = i.start

            new_end = min(end, i.end)
            res.append((start, new_end))
            start = new_end

        # append the non mapped part.
        if start != end:
            res.append((start, end))

        return res


class Mapping(object):

    def __init__(self, line=None):
        if line:
            v = re.split(r'\s+', line)
            self.destination, self.source, self.length = [int(x) for x in v]

    @property
    def start(self):
        return self.source

    @property
    def end(self):
        return self.source + self.length

    def inside(self, v):
        return v >= self.start and v <= self.end

    def overlap(self, start, end):
        return self.inside(start) or self.inside(end)

    def map(self, s):
        if not self.inside(s):
            return s
        return self.destination + (s - self.source)

    def __repr__(self):
        return '(%d, %d) -> %d)' % (self.source, self.length, self.destination)


class Seeds(object):

    def __init__(self, line=None, seeds=[]):
        self.seeds = [Interval(x) for x in seeds]
        if line:
            _, s = re.split(r':\s+', line)
            seeds = [int(x) for x in re.split(r'\s+', s)] 
            self.seeds = [Interval(x) for x in zip(seeds[::2], seeds[1::2]) ]

    def map(self, intervals):
        res = []
        for s in self.seeds:
            res.extend(s.map(intervals))
        return Seeds(seeds=res)

    def min(self):
        return min(x.start for x in self.seeds)


def process_section(lines, start):
    mappings = []

    title = lines[start]
    i = start + 1
    
    while i < len(lines) and lines[i]:
        mappings.append(Mapping(lines[i]))
        i += 1
    
    return i, mappings


def process_data(data):
    lines = [x.rstrip() for x in data]
    seeds = Seeds(lines[0])

    i = 2
    while i < len(lines):
        i, mappings = process_section(lines, i)
        mappings.sort(key=lambda x: x.source)
        i += 1
        seeds = seeds.map(mappings)
    return seeds.min()


if __name__ == '__main__':
    res = process_data(open(sys.argv[1]))
    print('results: %d' % res)
