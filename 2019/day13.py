from collections import Counter

from int_code import run_program


def part1(program):
    outp = list(run_program(program))
    tile_ids = outp[2::3]
    counts = Counter(tile_ids)
    return counts[2]


def part2(program):
    pass


def main():
    with open('day13.txt') as file:
        int_codes = [int(x) for x in file.readline().split(',')]
        print(part1(int_codes))
        print(part2(int_codes))


if __name__ == '__main__':
    main()
