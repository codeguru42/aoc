from collections import defaultdict

from aocd import get_data


def parse_sets(sets):
    for s in sets:
        d = {"red": 0, "green": 0, "blue": 0}
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


def get_possible(games):
    for game_id, sets in games:
        possible = True
        for s in sets:
            if s["red"] > 12 or s["green"] > 13 or s["blue"] > 14:
                possible = False
        if possible:
            yield game_id


def part1(games):
    return sum(get_possible(games))


def part2(games):
    pass


def main():
    data = get_data(year=2023, day=2)
    parsed = parse(data)
    print(part1(parsed))
    print(part2(parsed))


if __name__ == "__main__":
    main()
