from dataclasses import dataclass

import pytest
from aocd import get_data


example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


@pytest.fixture
def cards():
    return list(parse(example))


@pytest.fixture
def card(request, cards):
    return cards[request.param]


@pytest.fixture
def expected_scores():
    return [8, 2, 2, 1, 0, 0]


def test_part1(cards):
    assert part1(cards) == 13


@pytest.mark.parametrize("i", list(range(6)))
def test_count_winners(cards, expected_scores, i):
    assert score(cards[i]) == expected_scores[i]


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


def count_winners(card: Card) -> int:
    return len(set(card.winning) & set(card.numbers))


def score(card: Card) -> int:
    count = count_winners(card)
    return 2 ** (count - 1) if count > 0 else 0


def part1(cards: list[Card]) -> int:
    return sum(score(c) for c in cards)


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
