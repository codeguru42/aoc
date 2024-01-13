import math
import re
import timeit

import pytest
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


@pytest.fixture
def parsed():
    return parse(example)


@pytest.fixture
def workflows(parsed):
    return parsed[0]


@pytest.fixture
def parts(parsed):
    return parsed[1]


def test_part1(workflows, parts):
    assert part1(workflows, parts) == 19114


def test_is_accepted(workflows, parts):
    results = ["A", "R", "A", "R", "A"]
    for part, result in zip(parts, results):
        print("\n", part, result)
        assert is_accepted(part, workflows) == (result == "A")


def parse_workflows(rules):
    for rule in rules:
        match = re.match(r"(\w+)\{([^}]*)}", rule)
        name, conditions = match.groups()
        rules = conditions.split(",")
        yield name, [parse_workflow(rule) for rule in rules[:-1]] + [
            {"result": rules[-1]}
        ]


def parse_workflow(rule):
    match = re.match(r"(\w+)([><])(\d+):(\w+)", rule)
    return {
        "attribute": match.group(1),
        "operator": match.group(2),
        "value": int(match.group(3)),
        "result": match.group(4),
    }


def parse_part_attributes(attributes):
    for attribute in attributes:
        name, value = attribute.split("=")
        yield name, int(value)


def parse_parts(parts):
    for part in parts:
        yield dict(parse_part_attributes(part[1:-1].split(",")))


def parse(data):
    workflows, parts = data.strip().split("\n\n")
    return dict(parse_workflows(workflows.splitlines())), list(
        parse_parts(parts.splitlines())
    )


def evaluate(rule, part):
    match rule:
        case {"attribute": attribute, "operator": operator, "value": value}:
            match operator:
                case "<":
                    return part[attribute] < value
                case ">":
                    return part[attribute] > value
        case _:
            return True


def is_accepted(part, workflows):
    curr = workflows["in"]
    while True:
        for rule in curr:
            if evaluate(rule, part):
                match rule["result"]:
                    case "A":
                        return True
                    case "R":
                        return False
                    case next:
                        curr = workflows[next]
                        break


def rating(part):
    return part["x"] + part["m"] + part["a"] + part["s"]


def part1(workflows, parts):
    return sum(rating(part) for part in parts if is_accepted(part, workflows))


def count(curr, ranges, workflows):
    for rule in curr:
        match rule:
            case {
                "attribute": attribute,
                "operator": operator,
                "value": value,
                "result": result,
            }:
                match operator:
                    case "<":
                        original = ranges[attribute]["max"]
                        ranges[attribute]["max"] = value
                        if result == "A":
                            return True
                        if result == "R":
                            return False
                        accepted = count(workflows[result], ranges, workflows)
                        if accepted:
                            return True
                        ranges[attribute]["max"] = original
                    case ">":
                        original = ranges[attribute]["min"]
                        ranges[attribute]["min"] = value
                        if result == "A":
                            return True
                        if result == "R":
                            return False
                        accepted = count(workflows[result], ranges, workflows)
                        if accepted:
                            return True
                        ranges[attribute]["max"] = original
            case {"result": "R"}:
                return False
            case {"result": "A"}:
                return True


def part2(workflows):
    curr = workflows["in"]
    ranges = {
        attribute: {
            "min": 1,
            "max": 4000,
        }
        for attribute in ["x", "m", "a", "s"]
    }
    count(curr, ranges, workflows)
    return math.prod(a["max"] - a["min"] + 1 for a in ranges.values())


def main():
    data = get_data(year=2023, day=19)
    workflows, parts = parse(data)
    print("Part 1:", timeit.timeit(lambda: print(part1(workflows, parts)), number=1))
    print("Part 2:", timeit.timeit(lambda: print(part2(workflows)), number=1))


if __name__ == "__main__":
    main()
