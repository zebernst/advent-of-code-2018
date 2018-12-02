from code import aoc
from code.utils import *
from itertools import groupby
from difflib import SequenceMatcher


def part1(data: str):
    twos, threes = 0, 0
    for id in data.strip().split():
        groups = [list(g) for k, g in groupby(sorted(id))]
        if [e for e in groups if len(e) == 2]:
            twos += 1
        if [e for e in groups if len(e) == 3]:
            threes += 1
    return twos * threes


def part2(data: str):
    ids = [e for e in data.strip().split()]
    ratios = []
    for i1, id1 in enumerate(ids):
        for i2, id2 in enumerate(ids):
            if i1 == i2:
                continue
            ratios.append((i1, i2, SequenceMatcher(None, id1, id2).ratio()))
    match = max(ratios, key=lambda t: t[2])
    return cat(ch for i, ch in enumerate(ids[match[0]]) if ids[match[1]][i] == ch)


if __name__ == '__main__':
    data = aoc.data(day=2)

    print("part 1:", part1(data))
    print("part 2:", part2(data))
