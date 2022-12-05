import re
from itertools import zip_longest

from aocd import get_data


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def parse_crates(lines):
    crates = [[] for _ in range((len(lines[0]) + 1) // 4)]
    for line in lines:
        for i, crate in enumerate(grouper(line, 4)):
            if crate[1] != ' ':
                crates[i].insert(0, crate[1])
    return crates


def parse_inst(lines):
    for line in lines:
        matches = re.match(r'move (\d+) from (\d+) to (\d)', line)
        yield [int(x) for x in matches.group(1, 2, 3)]


def parse(data):
    lines = data.split('\n')
    labels_index = lines.index(' 1   2   3   4   5   6   7   8   9 ')
    crate_lines = lines[:labels_index]
    inst_lines = lines[labels_index+2:]

    return parse_crates(crate_lines), list(parse_inst(inst_lines))


def part1():
    pass


def part2():
    pass


def main():
    data = get_data(year=2022, day=5)
    stacks, inst = parse(data)
    print(stacks)
    print(inst)
    answer1 = part1()
    print(answer1)
    answer2 = part2()
    print(answer2)


if __name__ == '__main__':
    main()
