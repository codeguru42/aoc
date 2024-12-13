import timeit

from aocd import get_data


def test_blink():
    stones = [125, 17]
    expected = [253000, 1, 7]
    assert list(blink(stones)) == expected


def parse(data):
    return [int(x) for x in data.strip().split()]


def blink(stones):
    for s in stones:
        match s:
            case 0:
                yield 1
            case _:
                str_s = str(s)
                digit_count = len(str_s)
                if digit_count % 2 == 0:
                    yield int(str_s[: digit_count // 2])
                    yield int(str_s[digit_count // 2 :])
                else:
                    yield s * 2024


def part1(stones):
    for _ in range(25):
        stones = list(blink(stones))
    return len(stones)


def part2(lines):
    pass


def main():
    with open("day11.txt") as f:
        data = f.read()
    parsed = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(parsed)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
