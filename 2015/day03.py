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


def count_houses(consume):
    filename = sys.argv[1]
    with open(filename) as file:
        for line in file:
            return len(consume(line))


def part1():
    def f(line):
        return set(houses(line))
    return count_houses(f)


def part2():
    def f(line):
        return set(houses(line[::2])) | set(houses(line[1::2]))
    return count_houses(f)


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
