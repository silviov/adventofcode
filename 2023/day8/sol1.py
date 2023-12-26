#!/usr/bin/python3
import sys
import re

Graph = dict[str, tuple[str, str]]
START = 'AAA'
END = 'ZZZ'
LEFT = 'L'
RIGHT = 'R'


def parse_line(line: str) -> tuple[str, str, str]:
    m = re.match(r'(\w\w\w) = \((\w\w\w), (\w\w\w)\)', line)
    return m.group(1), m.group(2), m.group(3)


def parse_map(lines: list[str]) -> Graph:
    res = {}
    for line in lines:
        name, left, right = parse_line(line)
        res[name] = (left, right)
    return res


def walk(start: str, graph: Graph, instructions: str) -> int:
    res = 0
    i = 0
    while start != END:
        if i >= len(instructions): i = 0
        next = graph[start]
        start = next[0] if instructions[i] == LEFT else next[1]
        i += 1
        res += 1
    return res


def process_data(data: list[str]) -> int:
    instructions = data[0]
    m = parse_map(data[2:])
    return walk(START, m, instructions)


if __name__ == '__main__':
    res = process_data(list(x.rstrip('\n') for x in open(sys.argv[1])))
    print('results: %d' % res)
