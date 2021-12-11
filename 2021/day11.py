def parse(file):
    for line in file:
        yield [int(c) for c in line.strip()]


def part1():
    pass


def part2():
    pass


def main():
    with open('day11.txt') as file:
        starting_energy = list(parse(file))
    print(starting_energy)
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
