from dataclasses import dataclass

from aocd import get_data


@dataclass
class Card:
    card_id: int
    winning: list[int]
    numbers: list[int]


def parse_numbers(numbers: str):
    return [int(n) for n in numbers.strip().split()]


def parse(data: str) -> list[Card]:
    lines = data.strip().split("\n")
    for line in lines:
        card, card_data = line.split(":")
        card_id = card.split(" ")[-1]
        winning, numbers = card_data.split("|")
        yield Card(
            card_id=card_id,
            winning=parse_numbers(winning),
            numbers=parse_numbers(numbers),
        )


def part1(lines):
    pass


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=4)
    parsed = list(parse(data))
    print(parsed)
    print(part1(parsed))
    print(part2(parsed))


if __name__ == "__main__":
    main()
