from dataclasses import dataclass

import pytest
from aocd import get_data

example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


@pytest.fixture
def data():
    return parse(example.strip())


def test_part1(data):
    seeds, maps = data
    assert part1(seeds, maps) == 35


@pytest.fixture(params=range(4))
def seed(request, data):
    expected_locations = [82, 43, 86, 35]
    seeds, _ = data
    return seeds[request.param], expected_locations[request.param]


def test_get_location(seed, data):
    _, maps = data
    assert get_location(seed[0], maps) == seed[1]


@dataclass
class Map:
    dest: int
    source: int
    len: int


def parse_map(map):
    lines = map.split("\n")
    for line in lines[1:]:
        dest, source, l = [int(x) for x in line.split()]
        yield Map(source=source, dest=dest, len=l)


def parse_maps(maps):
    for map in maps:
        yield list(parse_map(map))


def parse_seeds(seeds: str):
    _, seeds = seeds.split(":")
    return [int(s) for s in seeds.strip().split(" ")]


def parse(data):
    maps = data.split("\n\n")
    return parse_seeds(maps[0]), list(parse_maps(maps[1:]))


def sort_maps(maps):
    for map in maps:
        map.sort(key=lambda m: m.source)


def get_next(curr: int, map: list[Map]) -> int:
    for m in map:
        if m.source <= curr < m.source + m.len:
            return m.dest + curr - m.source
    return curr


def get_location(seed: int, maps: list[list[Map]]) -> int:
    curr = seed
    for map in maps:
        curr = get_next(curr, map)
    return curr


def part1(seeds: list[int], maps: list[list[Map]]):
    return min(get_location(seed, maps) for seed in seeds)


def part2(seeds, maps):
    pass


def main():
    data = get_data(year=2023, day=5)
    seeds, maps = parse(data)
    sort_maps(maps)
    print(part1(seeds, maps))
    print(part2(seeds, maps))


if __name__ == "__main__":
    main()
