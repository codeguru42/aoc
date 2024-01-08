import timeit

from aocd import get_data

from aoc import sliding_window


def test_predict_previous():
    history = [int(x) for x in "10  13  16  21  30  45".split("  ")]
    assert predict_previous(history) == 5


def parse(data):
    lines = data.split("\n")
    for line in lines:
        yield [int(n) for n in line.split()]


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


def predict_previous(history):
    ds = reversed(list(all_diffs(history)))
    prev = 0
    for d in ds:
        prev = d[0] - prev
    return prev


def part2(histories):
    return sum(predict_previous(history) for history in histories)


def main():
    data = get_data(year=2023, day=9)
    parsed = list(parse(data))
    print(part1(parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
