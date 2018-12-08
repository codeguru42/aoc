def parse():
    with open('day8.txt') as file:
        data = [int(x) for x in file.readline().split()]
        tree, remaining = parse_tree(data)
        assert len(remaining) == 0
        return tree


def parse_tree(data):
    tree = {'children': []}
    child_count = data[0]
    metadata_count = data[1]
    data = data[2:]
    for _ in range(child_count):
        child, data = parse_tree(data)
        tree['children'].append(child)
    tree['metadata'] = data[:metadata_count]
    return tree, data[metadata_count:]


def part1(tree):
    return sum(part1(child) for child in tree['children']) + \
        sum(tree['metadata'])


def part2(tree):
    return tree


def main():
    tree = parse()
    print(part1(tree))
    print(part2(tree))


if __name__ == "__main__":
    main()
