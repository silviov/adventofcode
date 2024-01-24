#!/usr/bin/python3
import sys
import re
import collections

P = collections.namedtuple('P', ['x', 'y'])

def calc_dist(s1: P, s2: P, empty_cols: set[int], empty_rows: set[int], multiplier: int) -> int:
    xs = sorted([s1.x, s2.x])
    ys = sorted([s1.y, s2.y])
    double_cols = sum(1 for x in empty_cols if xs[0] < x < xs[1])
    double_rows = sum(1 for y in empty_rows if ys[0] < y < ys[1])
    # print(xs, ys, double_cols, double_rows, empty_cols, empty_rows)
    return (xs[1] - xs[0]) + (ys[1] - ys[0]) + (double_cols + double_rows) * (multiplier - 1)


def process_data(data: list[str], multiplier: int) -> int:
    stars = []
    empty_cols = set(range(len(data[0])))
    empty_rows = set(range(len(data)))
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '#':
                stars.append(P(x, y))
                if y in empty_rows: empty_rows.remove(y)
                if x in empty_cols: empty_cols.remove(x)

    res = 0
    for i, s1 in enumerate(stars):
        for j, s2 in enumerate(stars[i+1:]):
            d = calc_dist(s1, s2, empty_cols, empty_rows, multiplier)
            res += d
            # print('%d (%d, %d), %d (%d, %d): %d' % (i+1, s1.x, s1.y, i+j+2, s2.x, s2.y, d))
    return res


if __name__ == '__main__':
    res = process_data([list(x.rstrip('\n')) for x in open(sys.argv[1])], int(sys.argv[2]))
    print('results: %d' % res)
