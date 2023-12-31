from collections import Counter

from aocd import get_data

from int_code import parse, run_program


def part1(program):
    outp = list(run_program(program))
    tile_ids = outp[2::3]
    counts = Counter(tile_ids)
    return counts[2]


def part2(instructions):
    score = 0
    add_quarters = [3, 0]
    program = run_program(add_quarters + instructions)
    next(program)
    x = program.send(2)
    try:
        while True:
            y = next(program)
            if (x, y) == (-1, 0):
                score = next(program)
            else:
                tile = next(program)
    except StopIteration:
        pass
    finally:
        return score


def main():
    data = get_data(year=2019, day=13)
    int_codes = parse(data)
    print(part1(int_codes))
    print(part2(int_codes))


if __name__ == "__main__":
    main()
