from aocd import get_data


def parse_sets(sets):
    for s in sets:
        d = {}
        cubes = s.split(",")
        for cube in cubes:
            count, color = cube.strip().split(" ")
            d[color] = int(count)
        yield d


def parse_line(line):
    game, cubes = line.split(":")
    game_id = game.split(" ")[1]
    sets = cubes.strip().split(";")
    return int(game_id), list(parse_sets(sets))


def parse(data):
    lines = data.split("\n")
    for line in lines:
        yield parse_line(line)


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=2)
    parsed = parse(data)
    print(list(parsed))
    print(part1(parsed))
    print(part2(parsed))


if __name__ == "__main__":
    main()
