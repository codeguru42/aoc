def parse():
    with open('day8.txt') as file:
        return file.readlines()


def calc_power(x, y, grid_serial_number):
    rack_id = x + 10
    power = (rack_id * y + grid_serial_number) * rack_id
    return (power // 100) % 10 - 5


def part1(steps):
    return steps


def part2(steps):
    return steps


def main():
    assert calc_power(3, 5, 8) == 4
    inp = parse()
    print(part1(inp))
    print(part2(inp))


if __name__ == "__main__":
    main()
