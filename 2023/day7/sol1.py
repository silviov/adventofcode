#!/usr/bin/python3
import sys
import re
import functools
import collections

CARDS = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

def card_value(c):
    if c in CARDS:
        return CARDS[c]
    return int(c)
    

def calculate_kind(hand):
    d = collections.defaultdict(int)
    for h in hand:
        d[h] += 1
    if len(d.keys()) == 5:
        return 0
    c = collections.defaultdict(int)
    for v in d.values():
        c[v] += 1
    if c[2] == 1 and c[3] == 0:
        return 1
    if c[2] == 2:
        return 2
    if c[3] == 1 and c[2] == 0:
        return 3
    if c[3] == 1 and c[2] == 1:
        return 4
    if c[4] == 1:
        return 5
    if c[5] == 1:
        return 6
    return -1


@functools.total_ordering
class Hand(object):

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.kind = calculate_kind(hand)

    def __lt__(self, other):
        if self.kind == other.kind:
            for s, o in zip(self.hand, other.hand):
                if s == o:
                    continue
                return card_value(s) < card_value(o)
        return self.kind < other.kind

    def __eq__(self, other):
        return self.hand == other.hand

    def __repr__(self):
        return self.hand


def parse_hands(line):
    res = []
    for l in line:
        h, b = re.split(r'\s+', l)
        res.append(Hand(h, b))
    return res


def process_data(data):
    hands = parse_hands(data)
    hands.sort()
    return sum((c+1) * h.bid for c, h in enumerate(hands))


if __name__ == '__main__':
    res = process_data(list(x.rstrip('\n') for x in open(sys.argv[1])))
    print('results: %d' % res)
