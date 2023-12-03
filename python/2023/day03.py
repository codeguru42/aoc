from dataclasses import dataclass

from aocd import get_data

example_schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_parse_part_numbers():
    pns = parse_part_numbers(example_schematic.split("\n"))
    expected = [
        PartNumber(part_number=467, position=(0, 0)),
        PartNumber(part_number=114, position=(0, 5)),
        PartNumber(part_number=35, position=(2, 2)),
        PartNumber(part_number=633, position=(2, 6)),
        PartNumber(part_number=617, position=(4, 0)),
        PartNumber(part_number=58, position=(5, 7)),
        PartNumber(part_number=592, position=(6, 2)),
        PartNumber(part_number=755, position=(7, 6)),
        PartNumber(part_number=664, position=(9, 1)),
        PartNumber(part_number=598, position=(9, 5)),
    ]
    assert list(pns) == expected


@dataclass
class PartNumber:
    part_number: int
    position: tuple[int, int]


def parse(data) -> list[str]:
    return data.split("\n")


def parse_part_numbers(schematic) -> list[PartNumber]:
    for i, line in enumerate(schematic):
        part_number = 0
        position = (-1, -1)
        for j, c in enumerate(line):
            if c.isdigit():
                if part_number == 0:
                    position = (i, j)
                part_number = 10 * part_number + int(c)
            elif part_number != 0:
                yield PartNumber(part_number=part_number, position=position)
                part_number = 0


def part1(games: list[str]):
    pass


def part2(games: list[str]):
    pass


def main():
    data = get_data(year=2023, day=3)
    parsed = list(parse(data))
    print(part1(parsed))
    print(part2(parsed))


if __name__ == "__main__":
    main()
