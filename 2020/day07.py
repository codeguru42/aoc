from collections import defaultdict

import re
import unittest

example = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


class TestParse(unittest.TestCase):
    def test_parse(self):
        expected = {
            'bright white': ['light red', 'dark orange', ],
            'muted yellow': ['light red', 'dark orange', ],
            'shiny gold': ['bright white', 'muted yellow', ],
            'faded blue': ['muted yellow', 'dark olive', 'vibrant plum', ],
            'dark olive': ['shiny gold', ],
            'vibrant plum': ['shiny gold', ],
            'dotted black': ['dark olive', 'vibrant plum', ],
            None: ['faded blue', 'dotted black', ]
        }
        actual = parse(example.splitlines())
        self.assertEqual(expected, actual)

    def test_parse2(self):
        example = 'light salmon bags contain 5 dark brown bags, 2 dotted coral bags, 5 mirrored turquoise bags.'
        expected = {
            'dark brown': ['light salmon', ],
            'dotted coral': ['light salmon', ],
            'mirrored turquoise': ['light salmon', ],
        }
        actual = parse(example.splitlines())
        self.assertEqual(expected, actual)


class TestCount(unittest.TestCase):
    def test_count(self):
        bags = parse(example.splitlines())
        actual = count('shiny gold', bags)
        self.assertEqual(4, actual)


def parse(file):
    no_bags = r'([a-z ]+) bags contain no other bags.'
    contains_bags = r'([a-z ]+) bags contain (.*)'
    color = r'(\d+) ([a-z ]+) bags?'
    bags = defaultdict(list)
    for line in file:
        no_bags_matches = re.fullmatch(no_bags, line.strip())
        if no_bags_matches:
            bags[None].append(no_bags_matches.group(1))
        else:
            contains_bags_matches = re.fullmatch(contains_bags, line.strip())
            bag_groups = contains_bags_matches.groups()
            for color_str in bag_groups[1].split(','):
                color_match = re.search(color, color_str)
                bag = color_match.group(2)
                if bag:
                    bags[bag].append(bag_groups[0])
    return bags


def bfs(graph, root):
    to_visit = graph[root]

    while to_visit:
        n = to_visit.pop()
        yield n
        to_visit.extend(graph[n])


def count(color, bags):
    return len(set(bfs(bags, color)))


def part1(bags):
    return count('shiny gold', bags)


def part2():
    pass


def main():
    with open('day07.txt') as file:
        bags = parse(file)
    print(part1(bags))
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
