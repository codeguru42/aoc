import re
from dataclasses import dataclass

from aocd import get_data


@dataclass
class Race:
    time: int
    distance: int


def parse(data):
    lines = data.split("\n")
    times, distances = [re.split(r"\s+", line) for line in lines]
    for t, d in zip(times[1:], distances[1:]):
        yield Race(time=int(t), distance=int(d))


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=6)
    parsed = list(parse(data))
    print(parsed)
    print(part1(parsed))
    print(part2(parsed))


if __name__ == "__main__":
    main()
