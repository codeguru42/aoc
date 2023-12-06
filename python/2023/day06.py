import math
import re
from collections.abc import Generator
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


def count_wins(race: Race) -> int:
    count = 0
    for a in range(race.time + 1):
        if a * (race.time - a) >= race.distance:
            count += 1
    return count


def part1(races):
    return math.prod(count_wins(race) for race in races)


def combine(nums):
    return int("".join(str(n) for n in nums))


def combine_races(races):
    t = combine(r.time for r in races)
    d = combine(r.distance for r in races)
    return Race(time=t, distance=d)


def part2(races):
    race = combine_races(races)
    return count_wins(race)


def main():
    data = get_data(year=2023, day=6)
    parsed = list(parse(data))
    print(parsed)
    print(part1(parsed))
    print(part2(parsed))


if __name__ == "__main__":
    main()
