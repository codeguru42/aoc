from collections import defaultdict


def parse_orbits(file):
    orbits = defaultdict(lambda: [])
    for line in file:
        o = line.strip().split(')')
        orbits[o[0]].append(o[1])
    return orbits


def part1(orbits):
    pass


def part2(orbits):
    pass


def main():
    with open('day06.txt') as file:
        orbits = parse_orbits(file)
        print(orbits)
    print(part1(file))
    print(part2(file))


if __name__ == '__main__':
    main()
