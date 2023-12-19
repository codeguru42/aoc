import re
import timeit

from aocd import get_data


example = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""


def parse_rules(rules):
    for rule in rules:
        match = re.match(r"(\w+)\{([^}]*)}", rule)
        name, conditions = match.groups()
        yield name, conditions.split(",")


def parse_part_attributes(attributes):
    for attribute in attributes:
        name, value = attribute.split("=")
        yield name, int(value)


def parse_parts(parts):
    for part in parts:
        yield dict(parse_part_attributes(part[1:-1].split(",")))


def parse(data):
    rules, parts = data.split("\n\n")
    return dict(parse_rules(rules.splitlines())), list(parse_parts(parts.splitlines()))


def part1(rules, parts):
    pass


def part2(rules, parts):
    pass


def main():
    data = get_data(year=2023, day=19)
    rules, parts = parse(data)
    print(rules)
    print(parts)
    print(part1(rules, parts))
    print(part2(rules, parts))
    print("Part 1:", timeit.timeit(lambda: part1(rules, parts), number=1))
    print("Part 2:", timeit.timeit(lambda: part2(rules, parts), number=1))


if __name__ == "__main__":
    main()
