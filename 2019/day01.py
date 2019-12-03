def calc_fuel(mass):
    return mass // 3 - 2


def part1(masses):
    return sum(calc_fuel(int(x)) for x in masses)


def main():
    with open('day01.txt') as file:
        print(part1(file))


if __name__ == '__main__':
    main()
