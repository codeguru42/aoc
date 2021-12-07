def calculate_fuel(positions, new_pos):
    return sum(abs(x - new_pos) for x in positions)


def part1(positions):
    return min(calculate_fuel(positions, i) for i in range(max(positions)))


def part2():
    pass


def main():
    with open('day07.txt') as file:
        positions = [int(x) for x in file.readline().strip().split(',')]
    print(part1(positions))
    print(part2())


if __name__ == '__main__':
    main()
