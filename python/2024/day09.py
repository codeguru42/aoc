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


def move_blocks(disk):
    while len(disk) > 0:
        match disk:
            case [*rest, "."]:
                disk = rest
            case [".", *rest, last]:
                yield last
                disk = rest
            case [block, *rest]:
                yield block
                disk = rest


def part1(disk_map):
    disk = list(build_disk(disk_map))
    defragged = list(move_blocks(disk))
    return sum(i * file_id for i, file_id in enumerate(defragged))


def part2(lines):
    pass


def main():
    data = get_data(year=2024, day=9)
    parsed = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
