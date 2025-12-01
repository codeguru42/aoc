import json
import timeit

from aocd import get_data


def parse(data):
    return json.loads(data)


def get_numbers(data):
    match data:
        case int(data):
            yield data
        case str(data):
            yield 0
        case list(data):
            for d in data:
                yield from get_numbers(d)
        case dict(data):
            for k, v in data.items():
                yield from get_numbers(v)


def get_not_red_numbers(data):
    match data:
        case int(data):
            yield data
        case str(data):
            yield 0
        case list(data):
            for d in data:
                yield from get_not_red_numbers(d)
        case dict(data):
            if "red" in data.values():
                yield 0
            else:
                for k, v in data.items():
                    yield from get_not_red_numbers(v)


def part1(data):
    return sum(get_numbers(data))


def part2(data):
    return sum(get_not_red_numbers(data))


def main():
    data = get_data(year=2015, day=12)
    parsed = parse(data)
    print(parsed)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
