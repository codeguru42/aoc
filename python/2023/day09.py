import collections
import timeit
from itertools import islice

from aocd import get_data


def parse(data):
    lines = data.split("\n")
    for line in lines:
        yield [int(n) for n in line.split()]


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n - 1), maxlen=n)
    for x in it:
        window.append(x)
        yield tuple(window)


def diffs(history):
    for x, y in sliding_window(history, 2):
        yield y - x


def all_diffs(history):
    nums = history
    while any(x != 0 for x in nums):
        yield nums
        nums = list(diffs(nums))


def predict_next(history):
    ds = all_diffs(history)
    return sum(d[-1] for d in ds)


def part1(histories):
    return sum(predict_next(history) for history in histories)


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=9)
    parsed = list(parse(data))
    print(part1(parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
