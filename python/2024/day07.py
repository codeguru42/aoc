import timeit

from aocd import get_data


def parse_equations(lines):
    for line in lines:
        result, terms = line.strip().split(":")
        yield int(result), tuple(int(term) for term in terms.strip().split())


def parse(data):
    lines = data.strip().splitlines()
    return list(parse_equations(lines))


def is_valid(result, terms):
    if len(terms) == 1:
        return result == terms[0]
    return is_valid(result - terms[0], terms[1:]) or is_valid(
        result // terms[0], terms[1:]
    )


def part1(equations):
    return sum(result for result, terms in equations if is_valid(result, terms))


def part2(lines):
    pass


def main():
    data = get_data(year=2024, day=7)
    equations = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(equations)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(equations)), number=1))


if __name__ == "__main__":
    main()
