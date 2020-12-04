def part1():
    for expense1 in read_expenses():
        for expense2 in read_expenses():
            if expense1 + expense2 == 2020:
                return expense1 * expense2


def part2():
    pass


def read_expenses():
    with open('day01.txt') as file:
        for line in file:
            yield int(line.strip())


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
