import re
from collections import Counter
from datetime import datetime


def parse():
    raw_guards = read_file()
    raw_guards.sort(key=lambda x: x['timestamp'])

    id_regex = re.compile(r'\d+')
    guards = []
    itr = iter(raw_guards)
    try:
        x = next(itr)
        while True:
            y = id_regex.search(x['data'])
            id = y.group(0)
            minutes = []
            asleep = next(itr)
            while not asleep['data'].startswith('Guard'):
                awake = next(itr)
                minutes.append({
                    'asleep': asleep['timestamp'].minute,
                    'awake': awake['timestamp'].minute,
                })
                asleep = next(itr)
            guards.append({
                'id': id,
                'minutes': minutes,
            })
            x = asleep
    except StopIteration:
        asleep_counts = {}
        for g in guards:
            counts = asleep_counts.get(g['id'], Counter())
            for c in g['minutes']:
                for m in range(c['asleep'], c['awake']):
                    counts[m] += 1
            asleep_counts[g['id']] = counts
        return asleep_counts


def read_file():
    with open('day4.txt') as file:
        guards = []
        for line in file:
            line_regex = re.compile(r'\[(.*)\] (.*)')
            groups = line_regex.match(line).groups()
            guards.append({
                'timestamp': datetime.strptime(groups[0], '%Y-%m-%d %H:%M'),
                'data': groups[1]
            })
        return guards


def part1():
    asleep_counts = parse()

    totals = []
    for id, counts in asleep_counts.items():
        totals.append({
            'id': id,
            'total': len(list(counts.elements())),
        })

    m = max(totals, key=lambda x: x['total'])
    most_common = asleep_counts[m['id']].most_common(1)
    return int(m['id']) * most_common[0][0]


def part2():
    asleep_counts = parse()
    max_minutes = {
        guard_id: counts.most_common(1)
        for guard_id, counts in asleep_counts.items()
    }
    ms = [x for x in max_minutes.items() if x[1]]
    m = max(ms, key=lambda x: x[1][0][1])
    return int(m[0]) * m[1][0][0]


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
