def parse():
    with open('day6.txt') as file:
        return [(int(x), int(y)) for x, y in [line.split(',') for line in file]]


def part1(points):
    return points


def part2(points):
    return points


def main():
    points = parse()
    print(part1(points))
    print(part2(points))


if __name__ == "__main__":
    main()
