import string
from itertools import zip_longest

from aocd import get_data


def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')


def parse(data):
    return data.split()


def priority(item):
    p = ord(item.lower()) - ord('a') + 1
    if item.isupper():
        p += 26
    return p


def part1(sacks):
    total = 0
    for sack in sacks:
        n = len(sack)
        c1 = set(sack[:int(n/2)])
        c2 = set(sack[int(n/2):])
        both = c1 & c2
        for item in both:
            total += priority(item)
    return total


def part2(sacks):
    total = 0
    for group in grouper(sacks, 3):
        x, = set(string.ascii_letters).intersection(*(set(x) for x in group))
        total += priority(x)
    return total


def main():
    data = get_data(year=2022, day=3)
    supplies = parse(data)
    answer1 = part1(supplies)
    print(answer1)
    answer2 = part2(supplies)
    print(answer2)


if __name__ == '__main__':
    main()
