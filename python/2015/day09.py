import itertools
from collections import defaultdict


def part1(graph):
    paths = itertools.permutations(graph.keys())
    return min(path_length(graph, p) for p in paths)


def part2(graph):
    paths = itertools.permutations(graph.keys())
    return max(path_length(graph, p) for p in paths)


def parse(file):
    graph = defaultdict(defaultdict)
    for line in file:
        e = line.strip().split(' = ')
        v = e[0].split(' to ')
        graph[v[0]][v[1]] = int(e[1])
        graph[v[1]][v[0]] = int(e[1])
    return graph


def path_length(graph, path):
    return sum(graph[v1][v2] for v1, v2 in itertools.pairwise(path))


def main():
    with open('day09.txt') as file:
        graph = parse(file)
        print(part1(graph))
        print(part2(graph))


if __name__ == '__main__':
    main()
