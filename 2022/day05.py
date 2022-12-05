import re
import unittest
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
    stack_count = (len(lines[0]) + 1) // 4
    labels = ' '.join(f' {i} ' for i in range(1, stack_count + 1))
    labels_index = lines.index(labels)
    crate_lines = lines[:labels_index]
    inst_lines = lines[labels_index+2:]

    return parse_crates(crate_lines), list(parse_inst(inst_lines))


example = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''


class TestPart1(unittest.TestCase):
    def test_part1(self):
        stacks, inst = parse(example)
        result = part1(stacks, inst)
        self.assertEqual('CMZ', result)


def part1(stacks, inst):
    for count, stack_from, stack_to in inst:
        stacks[stack_to - 1] += reversed(stacks[stack_from - 1][-count:])
        stacks[stack_from - 1] = stacks[stack_from - 1][:-count]

    return ''.join(stack[-1] for stack in stacks)


class TestPart2(unittest.TestCase):
    def test_part2(self):
        stacks, inst = parse(example)
        result = part2(stacks, inst)
        self.assertEqual('MCD', result)


def part2(stacks, inst):
    for count, stack_from, stack_to in inst:
        stacks[stack_to - 1] += stacks[stack_from - 1][-count:]
        stacks[stack_from - 1] = stacks[stack_from - 1][:-count]

    return ''.join(stack[-1] for stack in stacks)


def main():
    data = get_data(year=2022, day=5)
    stacks, inst = parse(data)
    answer1 = part1(stacks, inst)
    print(answer1)
    answer2 = part2(stacks, inst)
    print(answer2)


if __name__ == '__main__':
    main()
