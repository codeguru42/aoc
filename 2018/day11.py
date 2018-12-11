import itertools

import numpy as np


def calc_power(x, y, grid_serial_number):
    rack_id = x + 10
    power = (rack_id * y + grid_serial_number) * rack_id
    return (power // 100) % 10 - 5


def part1(grid_serial_number):
    coords = itertools.product(range(301), range(301))
    power = [
        calc_power(x, y, grid_serial_number) for x, y in coords
    ]
    power_2d = np.array(power)
    power_2d.shape = (301, 301)
    return power_2d


def part2():
    return None


def main():
    assert calc_power(3, 5, 8) == 4

    grid_serial_number = 1723
    print(part1(grid_serial_number))
    print(part2())


if __name__ == "__main__":
    main()
