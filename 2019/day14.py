def parse_reactions(file):
    reactions = {}

    for line in file:
        reactants, product = line.strip().split('=>')
        reactants = [r.split() for r in reactants.split(',')]
        amt, p = product.split()
        reactions[p] = amt, reactants
    return reactions


def part1(reactions):
    pass


def part2(reactions):
    pass


def main():
    with open('day14.txt') as file:
        reactions = parse_reactions(file)
        print(part1(reactions))
        print(part2(reactions))


if __name__ == '__main__':
    main()
