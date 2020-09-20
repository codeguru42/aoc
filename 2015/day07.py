def parse(lines):
    parsed = [line.strip().split('->') for line in lines]
    wires = {wire.strip(): op.strip().split() for op, wire in parsed}
    return wires


def part1():
    with open('day07.txt') as file:
        print(parse(file))


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
