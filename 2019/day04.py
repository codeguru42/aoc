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
        if is_password1(n):
            count += 1
    return count


def is_password1(n):
    has_double = False
    monotonic_increasing = True
    for a, b in pairwise(digits(n)):
        if a == b:
            has_double = True
        if a < b:
            monotonic_increasing = False
            break
    return has_double and monotonic_increasing


def part2(start, end):
    count = 0
    for n in range(start, end + 1):
        if is_password2(n):
            count += 1
    return count


def is_password2(n):
    has_double = False
    monotonic_increasing = True
    repeat_count = 1
    for a, b in pairwise(digits(n)):
        if a == b:
            repeat_count += 1
        else:
            if repeat_count == 2:
                has_double = True
            repeat_count = 1
        if a < b:
            monotonic_increasing = False
            break
    if repeat_count == 2:
        has_double = True
    return has_double and monotonic_increasing


def main():
    start = 246540
    end = 787419
    print(part1(start, end))
    print(part2(start, end))


if __name__ == '__main__':
    main()
