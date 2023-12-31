def calc_fuel(mass):
    return mass // 3 - 2


def calc_all_fuel(mass):
    fuel = 0
    mass = calc_fuel(mass)
    while mass > 0:
        fuel += mass
        mass = calc_fuel(mass)
    return fuel


def part1(masses):
    return sum(calc_fuel(int(x)) for x in masses)


def part2(masses):
    return sum(calc_all_fuel(int(x)) for x in masses)


def main():
    with open('day01.txt') as file:
        print(part1(file))
    with open('day01.txt') as file:
        print(part2(file))


if __name__ == '__main__':
    main()
