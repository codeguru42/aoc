from itertools import tee


def digits(n):
    while n > 0:
        yield n % 10
        n //= 10


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def part1(start, end):
    count = 0
    for n in range(start, end + 1):
        has_double = False
        monotonic_increasing = True
        for a, b in pairwise(digits(n)):
            if a == b:
                has_double = True
            if a < b:
                monotonic_increasing = False
        if has_double and monotonic_increasing:
            count += 1
    return count


def part2(start, end):
    pass


def main():
    start = 246540
    end = 787419
    print(part1(start, end))
    print(part2(start, end))


if __name__ == '__main__':
    main()
