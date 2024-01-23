#!/usr/bin/python3
import sys
import re

class P(object):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return str((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


POINTS = {
    'N': P(0, -1),
    'S': P(0,  1),
    'W': P(-1, 0),
    'E': P( 1, 0),
}

OPPOSITE = {
    'N': 'S',
    'S': 'N',
    'W': 'E',
    'E': 'W',
}

DIRECTIONS = {
    '|': 'NS',
    '-': 'EW',
    'L': 'NE',
    'J': 'NW',
    '7': 'SW',
    'F': 'SE',
}


def get_char(data: list[str], p: P) -> str:
    return data[p.y][p.x]


def set_char(data: list[str], p: P, s: str):
    data[p.y][p.x] = s


def is_inside(data: list[str], p: P) -> bool:
    return p.x >= 0 and p.x < len(data[0]) and p.y >= 0 and p.y < len(data)


def find_start(data: list[str]) -> tuple[tuple[int, int], str]:
    start = P(-1, -1)
    direction = []
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            if c == 'S':
                start = P(x, y)

    if start == P(-1, -1):
        raise RuntimeError('did not find start in the provided data')

    for d, coord in POINTS.items():
        n = start + coord
        if not is_inside(data, n):
            continue
        c = get_char(data, n)
        if c not in DIRECTIONS:
            continue
        if OPPOSITE[d] in DIRECTIONS[c]:
            direction.append(d)

    direction.sort()
    connections = ''.join(direction)
    letter = ''
    for d, c in DIRECTIONS.items():
        if connections == ''.join(sorted(c)):
            letter = d
            break
    set_char(data, start, letter)

    return start, letter



def count_inside(data: list[str], pipe: set[P]) -> int:
    res = 0

    for y, line in enumerate(data):
        inside = False
        previous_angle = ''
        for x, c in enumerate(line):
            p = P(x, y)
            if p not in pipe:
                if inside:
                    res += 1
                continue

            if c == '-':
                continue

            if c == '|':
                inside = not inside
                continue

            if c == 'F' or c == 'L':
                previous_angle = c
                continue

            if (c == 'J' and previous_angle == 'F') or (c == '7' and previous_angle == 'L'):
                previous_angle = ''
                inside = not inside
                continue
            
    return res


def process_data(data: list[str]) -> int:
    start, letter = find_start(data)
    pipe = set()

    queue = []
    for c in DIRECTIONS[letter]:
        queue.append((start, 0, c))

    while queue:
        curr, n, direction = queue.pop(0)
        pipe.add(curr)
        next = curr + POINTS[direction]
        c = get_char(data, next)
        if next in pipe:
            break
        next_directions = set(DIRECTIONS[c])
        next_directions.remove(OPPOSITE[direction])
        queue.append((next, n+1, ''.join(next_directions)))

    return count_inside(data, pipe)


if __name__ == '__main__':
    res = process_data([list(x.rstrip('\n')) for x in open(sys.argv[1])])
    print('results: %d' % res)
