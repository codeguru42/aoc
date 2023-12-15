import timeit

import pytest
from aocd import get_data


@pytest.mark.parametrize(
    "step,expected",
    [
        ("rn=1", 30),
        ("cm-", 253),
        ("qp=3", 97),
        ("cm=2", 47),
        ("qp-", 14),
        ("pc=4", 180),
        ("ot=9", 9),
        ("ab=5", 197),
        ("pc-", 48),
        ("pc=6", 214),
        ("ot=7", 231),
    ],
)
def test_elf_hash(step, expected):
    assert elf_hash(step) == expected


def elf_hash(step):
    result = 0
    for c in step:
        result = (result + ord(c)) * 17 % 256
    return result


def parse(data):
    return data.split(",")


def part1(steps):
    return sum(elf_hash(step) for step in steps)


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=15)
    parsed = parse(data)
    print(part1(parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
