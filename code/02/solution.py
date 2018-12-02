from code import aoc
from code.utils import *
from itertools import groupby


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
    ids = data.strip().split()
    common = []
    for i1, id1 in enumerate(ids):
        for i2, id2 in enumerate(ids):
            if i1 == i2:
                continue
            common.append(cat(ch for i, ch in enumerate(id1) if id2[i] == ch))

    return max(common, key=len)


if __name__ == '__main__':
    data = aoc.data(day=2)

    print("part 1:", part1(data))
    print("part 2:", part2(data))
