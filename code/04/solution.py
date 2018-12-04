from code import aoc
from code.utils import *
import re
from datetime import datetime, timedelta
from itertools import groupby, chain
from collections import Counter


def parse_log(data: str):
    guard_log = []
    guard_id = None
    fell_asleep = None
    for entry in sorted(data.split('\n')):
        m = re.compile(r"\[(\d+-\d+-\d+) (\d+:\d+)\] (.*)").match(entry)
        if 'guard' in m.group(3).lower():
            guard_id = m.group(3).split(' ')[1][1:]
            continue
        if 'asleep' in m.group(3).lower():
            fell_asleep = datetime.strptime(m.group(2), '%H:%M')
            continue
        if 'wakes' in m.group(3).lower():
            woke_up = datetime.strptime(m.group(2), '%H:%M')
            duration = woke_up - fell_asleep
            mins_asleep = [(fell_asleep + timedelta(minutes=m)).minute for m in range(int(duration.seconds / 60))]
            guard_log.append({'id': guard_id, 'asleep': mins_asleep})
            continue

    return [{'id': int(k), 'asleep': list(chain.from_iterable(e.get('asleep') for e in grp))}
            for k, grp in groupby(sorted(guard_log, key=lambda e: e.get('id')), key=lambda e: e.get('id'))]


def part1(data: str):
    guards = parse_log(data)
    sleepy_guard = max(guards, key=lambda e: len(e.get('asleep')))
    hours = sleepy_guard.get('asleep')
    return sleepy_guard.get('id') * max(hours, key=hours.count)


def part2(data: str):
    guards = parse_log(data)
    modes = [(guard.get('id'), *Counter(guard.get('asleep')).most_common(1)[0]) for guard in guards]
    predictable = max(modes, key=lambda e: e[2])
    return predictable[0] * predictable[1]


if __name__ == '__main__':
    data = aoc.data(day=4)

    print("part 1:", part1(data))
    print("part 2:", part2(data))
