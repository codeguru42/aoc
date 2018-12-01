def part1():
    with open('day1.txt') as file:
        return sum(int(line) for line in file)


def partial_sums(l):
    s = 0
    while True:
        for x in l:
            yield s
            s += x


def part2():
    frequencies = set()
    with open('day1.txt') as file:
        offsets = [int(x) for x in file]

    for p in partial_sums(offsets):
        if p in frequencies:
            return p
        frequencies.add(p)


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
