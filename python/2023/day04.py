from aocd import get_data


def parse(data):
    return data.split()


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=4)
    print(data)
    parsed = parse(data)
    print(part1(parsed))
    print(part2(parsed))


if __name__ == "__main__":
    main()
