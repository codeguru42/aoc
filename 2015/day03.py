import sys


def houses(directions):
    x, y = 0, 0
    yield x, y
    for d in directions:
        if d == '>':
            x += 1
        elif d == '<':
            x -= 1
        elif d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        yield x, y


def part1():
    filename = sys.argv[1]
    with open(filename) as file:
        for line in file:
            print(len(set(houses(line))))


def part2():
    filename = sys.argv[1]
    with open(filename) as file:
        for line in file:
            santa = set(houses(line[::2]))
            robo_santa = set(houses(line[1::2]))
            print(len(santa | robo_santa))


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
