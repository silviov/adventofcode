#!/usr/bin/python3
import sys
import collections
import re

Number = collections.namedtuple('Number', ['value', 'start', 'end'])


class Line(object):

    def __init__(self, line):
        self.symbols = set()
        self.numbers = []
        self.parse_line(line)

    def parse_line(self, line):
        for m in re.finditer('(\d+)', line):
            self.numbers.append(Number(
                value=int(m.group(0)), start=m.start(0), end=m.end(0)))

        for i, c in enumerate(line):
            if not c.isnumeric() and c not in ['.', '\n']:
                self.symbols.add(i)

    def has_symbol(self, start, end):
        return any( (start -1) <= x <= end for x in self.symbols)


class Map(object):

    def __init__(self):
        self.lines = []

    def read_data(self, lines):
        for i, l in enumerate(lines):
            self.lines.append(Line(l))

    def check_number(self, lnum, start, end):
        for c in range(lnum-1, lnum+2):
            if c >= 0 and c < len(self.lines):
                if self.lines[c].has_symbol(start, end):
                    return True
        return False

    def result(self):
        res = 0
        for i, l in enumerate(self.lines):
            for n in l.numbers:
                if self.check_number(i, n.start, n.end):
                    res += n.value
        return res


def process(filename):
    m = Map()
    m.read_data(open(filename))
    print("result: %d" % m.result())

if __name__ == '__main__':
    process(sys.argv[1])
