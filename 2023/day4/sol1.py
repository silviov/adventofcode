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
    if len(won) == 0:
        return 0
    return pow(2, len(won)-1)
    

def process_data(data):
    return sum(parse_line(l) for l in data)


if __name__ == '__main__':
    res = process_data(open(sys.argv[1]))
    print('results: %d' % res)
