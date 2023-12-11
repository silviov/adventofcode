#!/usr/bin/python3
import sys
import collections
import re

COLORS = ['blue', 'red', 'green']

def is_impossible(r, maxgame):
    return any(r[c] > maxgame[c] for c in COLORS)

def parse_game(line):
    res = []
    game, rounds = line.split(': ')

    m = re.match(r'Game (\d+)', game)
    n = int(m.groups()[0])

    for round in rounds.split('; '):
        d = {c: 0 for c in COLORS}
        for s in round.split(', '):
            m = re.match(r'(\d+) (\w+)', s)
            p, c = m.groups()
            d[c] += int(p)
        res.append(d)
    return n, res

def process_data(lines):
    res = 0
    for l in lines:
        n, rounds = parse_game(l)
        n = 1
        for c in COLORS:
            n *= max(r[c] for r in rounds)
        res += n
    return res


def process(filename):
    res = process_data(open(filename))
    print("result: %d" % res)

if __name__ == '__main__':
    process(sys.argv[1])
