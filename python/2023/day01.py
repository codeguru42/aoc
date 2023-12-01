from aocd import get_data


def parse(data):
    return data.split()


def part1(lines):
    return sum(digits1(lines))


def digits1(lines):
    for line in lines:
        digits = [c for c in line if c.isdigit()]
        yield int(digits[0] + digits[-1])


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=1)
    parsed = parse(data)
    print(part1(parsed))
    print(part2(parsed))


if __name__ == '__main__':
    main()
