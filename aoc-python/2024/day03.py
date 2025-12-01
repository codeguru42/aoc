import re
import timeit

from aocd import get_data


def parse_muls(data):
    for match in re.finditer(r"mul\((\d+),(\d+)\)", data):
        yield int(match.group(1)), int(match.group(2))


def part1(data):
    return sum(x * y for x, y in parse_muls(data))


def parse_muls2(data):
    enabled = True
    for match in re.finditer(r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", data):
        if match.group(1) == "mul":
            if enabled:
                yield int(match.group(2)), int(match.group(3))
        if match.group(4) == "do":
            enabled = True
        if match.group(5) == "don't":
            enabled = False


def part2(data):
    return sum(x * y for x, y in parse_muls2(data))


def main():
    data = get_data(year=2024, day=3)
    print("Part 1:", timeit.timeit(lambda: print(part1(data)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(data)), number=1))


if __name__ == "__main__":
    main()
