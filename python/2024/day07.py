import math
import timeit

import pytest
from aocd import get_data
from numpy.core.numeric import True_

test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


@pytest.fixture
def equations():
    return parse(test_input)


def test_part1(equations):
    assert part1(equations) == 3749


def test_part2(equations):
    assert part2(equations) == 11387


def parse_equations(lines):
    for line in lines:
        result, terms = line.strip().split(":")
        yield int(result), tuple(int(term) for term in terms.strip().split())


def parse(data):
    lines = data.strip().splitlines()
    return list(parse_equations(lines))


@pytest.mark.parametrize(
    "equation,expected",
    zip(
        parse(test_input),
        [
            True,
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            True,
        ],
    ),
)
def test_is_valid(equation, expected):
    assert is_valid(equation[0], equation[1]) == expected


@pytest.mark.parametrize(
    "equation,expected",
    zip(
        parse(test_input),
        [
            True,
            True,
            False,
            True,
            True,
            False,
            True,
            False,
            True,
        ],
    ),
)
def test_is_valid2(equation, expected):
    assert is_valid2(equation[0], equation[1]) == expected


def is_valid(result, terms):
    if len(terms) == 1:
        return result == terms[0]
    return is_valid(result - terms[-1], terms[:-1]) or is_valid(
        result / terms[-1], terms[:-1]
    )


def part1(equations):
    return sum(result for result, terms in equations if is_valid(result, terms))


def is_valid2(result, terms):
    if len(terms) == 1:
        return result == terms[0]
    num_digits = math.floor(math.log10(terms[-1])) + 1
    return (
        is_valid2(result - terms[-1], terms[:-1])
        or is_valid2(result / terms[-1], terms[:-1])
        or (
            terms[-1] == result % (10**num_digits)
            and is_valid2(result // (10**num_digits), terms[:-1])
        )
    )


def part2(equations):
    return sum(result for result, terms in equations if is_valid2(result, terms))


def main():
    data = get_data(year=2024, day=7)
    equations = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(equations)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(equations)), number=1))


if __name__ == "__main__":
    main()
