import itertools


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(itertools.islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def part1(numbers):
    for w in window(numbers, n=26):
        pre = w[:25]
        number = w[25]
        pairs = list(itertools.combinations(pre, 2))
        if number not in (sum(x) for x in pairs):
            return number


def part2():
    pass


def main():
    with open('day09.txt') as file:
        numbers = [int(line.strip()) for line in file]
    print(part1(numbers))
    print(part2())


if __name__ == '__main__':
    main()
