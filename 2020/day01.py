from itertools import combinations


def part1():
    for expense1, expense2 in combinations(read_expenses(), 2):
        if expense1 + expense2 == 2020:
            return expense1 * expense2


def part2():
    for expense1, expense2, expense3 in combinations(read_expenses(), 3):
        if expense1 + expense2 + expense3 == 2020:
            return expense1 * expense2 * expense3


def read_expenses():
    with open('day01.txt') as file:
        for line in file:
            yield int(line.strip())


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
