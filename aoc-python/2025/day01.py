import timeit

from aocd import get_data


def parse(data):
    for line in data.splitlines():
        first = line.strip()[0]
        rest = line.strip()[1:]
        match first:
            case "R":
                yield int(rest)
            case "L":
                yield -int(rest)
            case _:
                raise ValueError(f"Unexpected line {line}")


def part1(lines):
    position = 50
    count = 0
    for line in lines:
        position += line
        if position % 100 == 0:
            count += 1
    return count


def part2(lines):
    position = 50
    count = 0
    for line in lines:
        position += line
        count += abs(position // 100)
        # if position <= 0 or position >= 100:
        #     count += 1
        position %= 100
        print(line, position, count)
    return count


def main():
    data = get_data(year=2025, day=1)
    parsed = list(parse(data))
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
