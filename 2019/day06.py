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


def find_path(current, destination, orbits):
    if current == destination:
        return [current]
    for next_planet in orbits[current]:
        path = find_path(next_planet, destination, orbits)
        if path:
            return [current, *path]


def find_path_from_root(planet, orbits):
    return find_path('COM', planet, orbits)


def find_common_root(path1, path2):
    common = None
    for x, y in zip(path1, path2):
        if x == y:
            common = x
    return common


def part1(orbits):
    return count_orbits('COM', orbits, 0)


def part2(orbits):
    you = find_path_from_root('YOU', orbits)
    print(you)
    santa = find_path_from_root('SAN', orbits)
    print(santa)
    common = find_common_root(you, santa)
    common_path = find_path_from_root(common, orbits)
    print(common_path)
    return (len(you) - len(common_path)) + (len(santa) - len(common_path)) -2


def main():
    with open('day06.txt') as file:
        orbits = parse_orbits(file)
        print(orbits)
        print(orbits['COM'])
    print(part1(orbits))
    print(part2(orbits))


if __name__ == '__main__':
    main()
