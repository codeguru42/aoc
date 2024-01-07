import math
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
    schematic, parts = parse(example_schematic)
    expected = [
        Part(part_number=467, position=(0, 0)),
        Part(part_number=114, position=(0, 5)),
        Part(part_number=35, position=(2, 2)),
        Part(part_number=633, position=(2, 6)),
        Part(part_number=617, position=(4, 0)),
        Part(part_number=58, position=(5, 7)),
        Part(part_number=592, position=(6, 2)),
        Part(part_number=755, position=(7, 6)),
        Part(part_number=664, position=(9, 1)),
        Part(part_number=598, position=(9, 5)),
    ]
    assert list(parts) == expected


def test_is_pn():
    schematic, parts = parse(example_schematic)
    part = Part(part_number=467, position=(0, 0))
    assert is_pn(part, schematic)


def test_is_not_pn():
    schematic, parts = parse(example_schematic)
    part = Part(part_number=114, position=(0, 5))
    assert not is_pn(part, schematic)


def test_part1():
    schematic, parts = parse(example_schematic)
    result = part1(schematic, parts)
    expected = 4361
    assert result == expected


@dataclass
class Part:
    part_number: int
    position: tuple[int, int]


def parse(data) -> tuple[list[str], list[Part]]:
    lines = data.strip().split("\n")
    return lines, parse_part_numbers(lines)


def parse_part_numbers(schematic) -> list[Part]:
    for i, line in enumerate(schematic):
        part_number = 0
        position = (-1, -1)
        for j, c in enumerate(line):
            if c.isdigit():
                if part_number == 0:
                    position = (i, j)
                part_number = 10 * part_number + int(c)
            elif part_number != 0:
                yield Part(part_number=part_number, position=position)
                part_number = 0
        if part_number != 0:
            yield Part(part_number=part_number, position=position)


def is_pn(part: Part, schematic: list[str]):
    h = len(schematic)
    w = len(schematic[0])
    r, c = part.position
    l = 1 + math.floor(math.log(part.part_number, 10))
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + l + 1):
            if i == r and c - 1 < j < c + l:
                continue
            if 0 <= i < h and 0 <= j < w:
                sym = schematic[i][j]
                if not sym.isdigit() and sym != ".":
                    return True
    return False


def part1(schematic: list[str], parts: list[Part]):
    return sum(part.part_number for part in parts if is_pn(part, schematic))


def part2(schematic: list[str], parts: list[Part]):
    pass


def main():
    data = get_data(year=2023, day=3)
    schematic, parts = list(parse(data))
    print(part1(schematic, parts))
    print(part2(schematic, parts))


if __name__ == "__main__":
    main()
