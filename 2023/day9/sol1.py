#!/usr/bin/python3
import sys
import re

def get_nextn(nums: list[int]) -> list[int]:
    if all(x == 0 for x in nums):
        return nums + [0]
    res = []
    for i in range(len(nums) - 1):
        res.append(nums[i+1] - nums[i])
    diffs = get_nextn(res)
    nums.append(diffs[-1] + nums[-1])
    return nums


def process_line(line: str) -> int:
    nums = [int(x) for x in re.split(r'\s+', line)]
    return get_nextn(nums)[-1]


def process_data(data: list[str]) -> int:
    res = 0
    for line in data:
        res += process_line(line)
    return res


if __name__ == '__main__':
    res = process_data(list(x.rstrip('\n') for x in open(sys.argv[1])))
    print('results: %d' % res)
