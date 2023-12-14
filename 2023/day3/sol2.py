#!/usr/bin/python3
import sys
import collections
import re

Number = collections.namedtuple('Number', ['value', 'start', 'end'])
Symbol = collections.namedtuple('Symbol', ['value', 'index'])


class Line(object):

    def __init__(self, line):
        self.symbols = []
        self.numbers = []
        self.parse_line(line)

    def parse_line(self, line):
        for m in re.finditer('(\d+)', line):
            self.numbers.append(Number(
                value=int(m.group(0)), start=m.start(0), end=m.end(0)))

        for i, c in enumerate(line):
            if not c.isnumeric() and c not in ['.', '\n']:
                self.symbols.append(Symbol(value=c, index=i))

    def parts_at(self, c):
        nums = []
        for n in self.numbers:
            if n.start-1 <= c <= n.end:
                nums.append(n)
        return nums


class Map(object):

    def __init__(self):
        self.lines = []

    def read_data(self, lines):
        for i, l in enumerate(lines):
            self.lines.append(Line(l))

    def check_star(self, l, c):
        nums = []
        for i in [l-1, l, l+1]:
            if i < 0 or i > len(self.lines):
                continue
            nums.extend(self.lines[i].parts_at(c))
        if len(nums) == 2:
            return nums[1].value * nums[0].value
        return 0

    def result(self):
        res = 0
        for i, l in enumerate(self.lines):
            for s in l.symbols:
                if s.value == '*':
                    res += self.check_star(i, s.index)
        return res


def process(filename):
    m = Map()
    m.read_data(open(filename))
    print("result: %d" % m.result())

if __name__ == '__main__':
    process(sys.argv[1])
