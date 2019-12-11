from collections import defaultdict


def parse_orbits(file):
    orbits = defaultdict(lambda: [])
    for line in file:
        o = line.strip().split(')')
        orbits[o[0]].append(o[1])
    return orbits


def count_orbits(planet, orbits, count):
    if not orbits[planet]:
        return count
    return sum(count_orbits(p, orbits, count + 1) for p in orbits[planet]) + count


def part1(orbits):
    return count_orbits('COM', orbits, 0)


def part2(orbits):
    pass


def main():
    with open('day06.txt') as file:
        orbits = parse_orbits(file)
        print(orbits)
        print(orbits['COM'])
    print(part1(orbits))
    print(part2(orbits))


if __name__ == '__main__':
    main()
