def part1():
    with open('day07.txt') as file:
        parsed = [line.strip().split('->') for line in file]
        wires = {wire.strip(): op.strip() for op, wire in parsed}
        print(wires)


def part2():
    pass


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
