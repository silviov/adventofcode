#!/usr/bin/python3
import sys
import collections
import re

COLORS = ['blue', 'red', 'green']
Game = collections.namedtuple('Game', ['n', 'blue', 'red', 'green'])

def parse_game(line):
    d = {c: 0 for c in COLORS}
    pattern = '|'.join(r'(?:(?P<%s>\d+) %s)' % c for c in COLORS)

    game, rounds = line.split(':')

    m = re.match(r'Game (\d+)', game)
    n = int(m.groups()[1])

    for round in rounds.split(';'):
        for s in round.split(','):
            m = re.match(pattern, s)
            for c in d:
                if c in m.groups():
                    d[c] += m.groups()[c]
    return Game(n=n, **d)

def process_data(lines):
    games = []
    for l in lines:
        games.append(parge_game(line))


def process(filename):
    process_data(open(filename))

if __name__ == '__main__':
    process(sys.argv[1])
