from collections import defaultdict


def part1():
    pass


def part2():
    pass


def parse(file):
    graph = defaultdict(defaultdict)
    for line in file:
        e = line.strip().split(' = ')
        v = e[0].split(' to ')
        graph[v[0]][v[1]] = int(e[1])
        graph[v[1]][v[0]] = int(e[1])
    return graph


def main():
    with open('day09.txt') as file:
        graph = parse(file)
        print(graph)
        print(part1())
        print(part2())


if __name__ == '__main__':
    main()
