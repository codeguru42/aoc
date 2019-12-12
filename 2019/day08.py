from collections import Counter
from itertools import zip_longest
from sys import maxsize


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def parse(file, size):
    return grouper(file, size)


def part1(layers):
    zeroes = maxsize
    ones_and_twos = 0
    for layer in layers:
        counts = Counter(layer)
        if counts['0'] < zeroes:
            zeroes = counts['0']
            ones_and_twos = counts['1'] * counts['2']
    return ones_and_twos


def part2(layers):
    pass


def main():
    layer_size = 25*6
    with open('day08.txt') as file:
        layers = parse(file.read().strip(), layer_size)
        print(part1(layers))
        print(part2(layers))


if __name__ == '__main__':
    main()
