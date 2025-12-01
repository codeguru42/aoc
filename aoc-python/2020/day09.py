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


def sums(numbers):
    total = 0
    for n in numbers:
        total += n
        yield total


def part2(numbers, target):
    rest = numbers
    while True:
        for i, s in enumerate(sums(rest)):
            if s == target:
                numbers2 = rest[0:i+1]
                return min(numbers2) + max(numbers2)
            if s > target:
                break
        rest = rest[1:]


def main():
    with open('day09.txt') as file:
        numbers = [int(line.strip()) for line in file]
    solution = part1(numbers)
    print(solution)
    print(part2(numbers, solution))


if __name__ == '__main__':
    main()
