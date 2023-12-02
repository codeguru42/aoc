from dataclasses import dataclass

from aocd import get_data


@dataclass
class GameSet:
    red: int = 0
    blue: int = 0
    green: int = 0


@dataclass
class Game:
    id: int
    game_sets: list[GameSet]


def parse_sets(sets: list[str]) -> list[GameSet]:
    for s in sets:
        d = {}
        cubes = s.split(",")
        for cube in cubes:
            count, color = cube.strip().split(" ")
            d[color] = int(count)
        yield GameSet(**d)


def parse_line(line: str) -> Game:
    game, cubes = line.split(":")
    game_id = game.split(" ")[1]
    sets = cubes.strip().split(";")
    return Game(id=int(game_id), game_sets=list(parse_sets(sets)))


def parse(data) -> list[Game]:
    lines = data.split("\n")
    for line in lines:
        yield parse_line(line)


def get_possible(games: list[Game]):
    for game in games:
        possible = True
        for s in game.game_sets:
            if s.red > 12 or s.green > 13 or s.blue > 14:
                possible = False
        if possible:
            yield game.id


def part1(games: list[Game]):
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
