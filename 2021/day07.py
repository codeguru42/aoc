def calculate_total_fuel(positions, new_pos):
    return sum(abs(x - new_pos) for x in positions)


def part1(positions):
    return min(calculate_total_fuel(positions, i) for i in range(max(positions)))


def calculate_total_fuel2(positions, new_pos):
    return sum(calculate_fuel(abs(x - new_pos)) for x in positions)


def calculate_fuel(steps):
    return steps * (steps + 1) / 2


def part2(positions):
    return min(calculate_total_fuel2(positions, i) for i in range(max(positions)))


def main():
    with open('day07.txt') as file:
        positions = [int(x) for x in file.readline().strip().split(',')]
    print(part1(positions))
    print(part2(positions))


if __name__ == '__main__':
    main()
