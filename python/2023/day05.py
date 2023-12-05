from dataclasses import dataclass

from aocd import get_data


@dataclass
class Map:
    dest: int
    source: int
    len: int


def parse_map(map):
    lines = map.split("\n")
    for line in lines[1:]:
        source, dest, l = [int(x) for x in line.split()]
        yield Map(source=source, dest=dest, len=l)


def parse_maps(maps):
    for map in maps[1:]:
        yield parse_map(map)


def parse_seeds(seeds: str):
    _, seeds = seeds.split(":")
    return [int(s) for s in seeds.strip().split(" ")]


def parse(data):
    maps = data.split("\n\n")
    return parse_seeds(maps[0]), list(parse_maps(maps[1:]))


def part1(seeds, maps):
    pass


def part2(seeds, maps):
    pass


def main():
    data = get_data(year=2023, day=5)
    seeds, maps = parse(data)
    print(seeds)
    for map in maps:
        print("----------")
        for m in map:
            print(m)
    print(part1(seeds, maps))
    print(part2(seeds, maps))


if __name__ == "__main__":
    main()
