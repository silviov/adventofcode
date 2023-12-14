#!/usr/bin/python3
import sys
import re

def parse_line(line):
    line = line.rstrip()
    name, parts = re.split(r':\s+', line)
    _, id = re.split(r'\s+', name)
    winning, had = re.split(r'\s+\|\s+', parts)
    winning = set(int(w) for w in re.split(r'\s+', winning))
    had = set(int(h) for h in re.split(r'\s+', had))
    won = winning & had
    return len(won)


def process_data(data):
    res = 0
    won = [parse_line(l) for l in data]
    counts = [1] * len(won)
    for i in range(len(won)):
        res += counts[i]
        for w in range(won[i]):
            counts[i + w + 1] += counts[i]
    return res


if __name__ == '__main__':
    res = process_data(open(sys.argv[1]))
    print('results: %d' % res)
