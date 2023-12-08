import enum
import timeit
from collections import Counter

import pytest
from aocd import get_data


class Rank(enum.IntEnum):
    HIGH_CARD = enum.auto()
    ONE_PAIR = enum.auto()
    TWO_PAIR = enum.auto()
    THREE_OF_A_KIND = enum.auto()
    FULL_HOUSE = enum.auto()
    FOUR_OF_A_KIND = enum.auto()
    FIVE_OF_A_KIND = enum.auto()


example = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


@pytest.fixture
def hands():
    return list(parse(example))


@pytest.fixture(params=range(5))
def hand(request, hands):
    return hands[request.param]


def test_part1(hands):
    assert part1(hands) == 6440


expected_keys = [
    (Rank.ONE_PAIR, [3, 2, 10, 3, 13]),
    (Rank.THREE_OF_A_KIND, [10, 5, 5, 11, 5]),
    (Rank.TWO_PAIR, [13, 13, 6, 7, 7]),
    (Rank.TWO_PAIR, [13, 10, 11, 11, 10]),
    (Rank.THREE_OF_A_KIND, [12, 12, 12, 11, 14]),
]
# @pytest.mark.parametrize("expected_key", expected_keys)


def test_key(hand):
    print("\n", hand)
    print(key1(hand[0]))


def order1(card):
    match card:
        case c if "2" <= c <= "9":
            return int(c)
        case "T":
            return 10
        case "J":
            return 11
        case "Q":
            return 12
        case "K":
            return 13
        case "A":
            return 14


def rank1(cards):
    counts = Counter(cards)
    counts_of_counts = Counter(counts.values())
    if counts_of_counts[5] == 1:
        return Rank.FIVE_OF_A_KIND
    if counts_of_counts[4] == 1:
        return Rank.FOUR_OF_A_KIND
    if counts_of_counts[3] == 1 and counts_of_counts[2] == 1:
        return Rank.FULL_HOUSE
    if counts_of_counts[3] == 1:
        return Rank.THREE_OF_A_KIND
    if counts_of_counts[2] == 2:
        return Rank.TWO_PAIR
    if counts_of_counts[2] == 1:
        return Rank.ONE_PAIR
    return Rank.HIGH_CARD


def key1(cards):
    card_order = [order1(card) for card in cards]
    rank = rank1(cards)
    return rank, card_order


def order2(card):
    match card:
        case c if "2" <= c <= "9":
            return int(c)
        case "T":
            return 10
        case "J":
            return 1
        case "Q":
            return 12
        case "K":
            return 13
        case "A":
            return 14


def rank2(cards):
    rank = rank1(cards)
    counts = Counter(cards)
    if rank == Rank.FOUR_OF_A_KIND and counts["J"] >= 1:
        return Rank.FIVE_OF_A_KIND
    if rank == Rank.FULL_HOUSE:
        if counts["J"] >= 2:
            return Rank.FIVE_OF_A_KIND
    if rank == Rank.THREE_OF_A_KIND:
        if counts["J"] == 3:
            return Rank.FOUR_OF_A_KIND
        if counts["J"] == 2:
            return Rank.FIVE_OF_A_KIND
        if counts["J"] == 1:
            return Rank.FOUR_OF_A_KIND
    if rank == Rank.TWO_PAIR:
        if counts["J"] == 1:
            return Rank.FULL_HOUSE
        if counts["J"] == 2:
            return Rank.FOUR_OF_A_KIND
    if rank == Rank.ONE_PAIR:
        if counts["J"] == 1:
            return Rank.THREE_OF_A_KIND
        if counts["J"] == 2:
            return Rank.THREE_OF_A_KIND
    if rank == Rank.HIGH_CARD:
        if counts["J"] == 1:
            return Rank.ONE_PAIR
    return rank


def key2(cards):
    card_order = [order2(card) for card in cards]
    rank = rank2(cards)
    return rank, card_order


def parse(data):
    lines = data.strip().split("\n")
    for line in lines:
        cards, bid = line.strip().split()
        yield cards, int(bid)


def score(hands, key):
    sorted_hands = sorted(hands, key=lambda x: key(x[0]))
    return sum(bid * rank for rank, (_, bid) in enumerate(sorted_hands, start=1))


def part1(hands):
    return score(hands, key1)


def part2(hands):
    return score(hands, key2)


def main():
    data = get_data(year=2023, day=7)
    parsed = list(parse(data))
    print(part1(parsed))
    print(part2(parsed))
    print("Part 1:", timeit.timeit(lambda: part1(parsed), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(parsed), number=1))


if __name__ == "__main__":
    main()
