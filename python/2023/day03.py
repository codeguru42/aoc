import math
from dataclasses import dataclass

import pytest
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


@pytest.fixture
def schematic():
    return parse(example_schematic)


def test_parse_part_numbers(schematic):
    pns = parse_part_numbers(schematic)
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


def test_is_pn(schematic):
    pn = PartNumber(part_number=467, position=(0, 0))
    assert is_pn(pn, schematic)


def test_is_not_pn(schematic):
    pn = PartNumber(part_number=114, position=(0, 5))
    assert not is_pn(pn, schematic)


def test_part1(schematic):
    result = part1(schematic)
    expected = 4361
    assert result == expected


@dataclass
class PartNumber:
    part_number: int
    position: tuple[int, int]


def parse(data) -> list[str]:
    return data.strip().split("\n")


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


def is_pn(pn: PartNumber, schematic: list[str]):
    print(pn)
    h = len(schematic)
    w = len(schematic[0])
    r, c = pn.position
    l = math.ceil(math.log(pn.part_number, 10))
    result = False
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + l + 1):
            if i == r and c - 1 < j < c + l:
                continue
            if 0 <= i < h and 0 <= j < w:
                print(i, j)
                sym = schematic[i][j]
                if not sym.isdigit() and sym != ".":
                    result = True
    print(result)
    return result


def part1(schematic: list[str]):
    part_numbers = parse_part_numbers(schematic)
    return sum(pn.part_number for pn in part_numbers if is_pn(pn, schematic))


def part2(games: list[str]):
    pass


def main():
    data = get_data(year=2023, day=3)
    parsed = list(parse(data))
    print(part1(parsed))
    print(part2(parsed))


if __name__ == "__main__":
    main()
