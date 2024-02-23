#!/usr/bin/python3
import sys
import re
import collections

GOOD = '.'
BAD  = '#'
UNK  = '?'

class Status(object):

    def __init__(self, latest_char=GOOD, count=0, pattern_pos=-1,
                 total_count=0):
        self.latest_char = latest_char
        self.count = count
        self.pattern_pos = pattern_pos
        self.total_count = total_count

    def try_next(self, c, pattern):
        s = Status(c, self.count, self.pattern_pos, self.total_count)
        if c == GOOD:
            if (self.latest_char == BAD and
                self.pattern_pos != -1 and
                pattern[self.pattern_pos] != self.count):
                return None

        if c == BAD:
            s.total_count += 1
            if self.latest_char == GOOD:
                s.count = 1
                s.pattern_pos += 1
                if s.pattern_pos >= len(pattern):
                    return None
            else:
                s.count += 1
                if s.count > pattern[s.pattern_pos]:
                    return None
        return s

    def add_char(self, c, pattern):
        res = []
        if c == UNK or c == GOOD:
            r = self.try_next(GOOD, pattern)
            if r: res.append(r)
        if c == UNK or c == BAD:
            r = self.try_next(BAD, pattern)
            if r: res.append(r)
        return res

    def __repr__(self):
        return '(%s, %d, %d)' % (self.latest_char, self.count, self.pattern_pos)

def process_line(pipe: list[str], pattern: list[int]) -> int:
    statuses = [Status()]
    tot = len(pipe)
    tot_bad = sum(pattern)
    d = {UNK:0, BAD:0, GOOD:0}
    for x in pipe:
        d[x] += 1

    for c in pipe:
        new_statuses = []
        for s in statuses:
            new_statuses.extend(s.add_char(c, pattern))
        statuses = [x for x in new_statuses if x.total_count <= tot_bad
        ]
    return len([
        s for s in statuses
        if s.pattern_pos == len(pattern) - 1 and
        s.count == pattern[-1]
        ])


def process_data(data: list[str], copies=1) -> int:
    res = 0
    for line in data:
        pipe, pattern = line.split()
        if copies > 1:
            pipe = '?'.join(copies * [pipe])
            pattern = ','.join(copies * [pattern])
        pipe = list(pipe)
        pattern = [int(x) for x in pattern.split(',')]
        res += process_line(pipe, pattern)
    return res


if __name__ == '__main__':
    res = process_data([x.rstrip('\n') for x in open(sys.argv[1])],
                       int(sys.argv[2]))
    print('results: %d' % res)
