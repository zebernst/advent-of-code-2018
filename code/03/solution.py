from code import aoc
from code.utils import *
import re
from itertools import chain
from collections import Counter


def part1(data: str):
    fabric = list(list([] for i in range(1000)) for j in range(1000))

    for claim in data.strip().split('\n'):
        p = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
        m = p.match(claim)
        cid, left, top, width, height = (int(e) for e in m.groups())
        for i, row in enumerate(fabric[top:top+height]):
            for j, col in enumerate(row[left:left+width]):
                fabric[top+i][left+j].append(cid)

    return len([e for e in chain(*fabric) if len(e) >= 2])


def part2(data: str):
    fabric = list([list() for i in range(1000)] for j in range(1000))
    claims = {}

    for claim in data.strip().split('\n'):
        p = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
        m = p.match(claim)
        cid, left, top, width, height = (int(e) for e in m.groups())
        claims[cid] = width * height
        for i, row in enumerate(fabric[top:top+height]):
            for j, col in enumerate(row[left:left+width]):
                fabric[top+i][left+j].append(cid)

    for k, c in Counter(chain(*(l for l in chain(*fabric) if len(l) == 1))).items():
        if claims[k] == c:
            return k


if __name__ == '__main__':
    data = aoc.data(day=3)

    print("part 1:", part1(data))
    print("part 2:", part2(data))
