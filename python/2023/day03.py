from aocd import get_data


def parse(data) -> list[str]:
    return data.split("\n")


def part1(games: list[str]):
    pass


def part2(games: list[str]):
    pass


def main():
    data = get_data(year=2023, day=3)
    parsed = parse(data)
    print(part1(parsed))
    print(part2(parsed))


if __name__ == "__main__":
    main()
