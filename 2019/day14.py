def parse_reactions(file):
    reactions = {}

    for line in file:
        reactants_str, product = line.strip().split('=>')
        reactants = []
        for r in reactants_str.split(','):
            x, y = r.strip().split()
            reactants.append((int(x), y))
        amt, p = product.split()
        reactions[p] = int(amt), reactants
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
