import timeit
from dataclasses import dataclass

from aocd import get_data


@dataclass
class Line:
    point: tuple[int, int, int]
    vector: tuple[int, int, int]


def parse(data):
    lines = data.splitlines()
    for line in lines:
        p, v = line.split("@")
        point = tuple(int(x.strip()) for x in p.strip().split(","))
        vector = tuple(int(x.strip()) for x in v.strip().split(","))
        yield Line(point=point, vector=vector)


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=24)
    parsed = list(parse(data))
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
