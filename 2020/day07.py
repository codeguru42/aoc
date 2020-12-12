import re


def parse(file):
    no_bags = r'([a-z ]+) bags contain no other bags.'
    contains_bags = r'([a-z ]+) bags contain (\d+) ([a-z ]+) bags?(, (\d+) ([a-z ]+) bags?)*\.'
    bags = {}
    for line in file:
        no_bags_matches = re.fullmatch(no_bags, line.strip())
        if no_bags_matches:
            bags[no_bags_matches.group(1)] = None
        else:
            contains_bags_matches = re.fullmatch(contains_bags, line.strip())
            bag_groups = contains_bags_matches.groups()
            bags[bag_groups[0]] = bag_groups[2::3]
    return bags


def part1():
    pass


def part2():
    pass


def main():
    with open('day07.txt') as file:
        bags = parse(file)
    print(bags)
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
