from aocd import get_data


def parse(data):
    elves = data.split('\n\n')
    for elf in elves:
        yield [int(x) for x in elf.split()]


def part1(elves):
    return max(sum(elf) for elf in elves)


def part2(elves):
    return sum(sorted(sum(elf) for elf in elves)[-3:])


def main():
    data = get_data(year=2022, day=1)
    parsed = list(parse(data))
    print(part1(parsed))
    print(part2(parsed))


if __name__ == '__main__':
    main()
