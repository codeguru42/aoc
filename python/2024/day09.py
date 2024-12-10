import timeit

from aocd import get_data

import aoc


def parse(data):
    return [int(x) for x in data.strip()]


def build_disk(disk_map):
    for file_id, (file_size, free_size) in enumerate(aoc.grouper(disk_map, 2)):
        for _ in range(file_size):
            yield file_id
        if free_size:
            for _ in range(free_size):
                yield "."


def part1(disk_map):
    disk = list(build_disk(disk_map))
    print(disk)


def part2(lines):
    pass


def main():
    data = get_data(year=2024, day=9)
    parsed = parse(data)
    print(parsed)
    print(sum(parsed))
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
