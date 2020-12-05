import collections


def part1(lines):
    valid_count = 0
    for line in lines:
        parts = line.split()
        min_count, max_count = parts[0].split('-')
        min_count = int(min_count)
        max_count = int(max_count)
        letter = parts[1][0]
        counts = collections.Counter(parts[2])
        if min_count <= counts[letter] <= max_count:
            valid_count += 1
    return valid_count


def part2():
    pass


def main():
    with open('day02.txt') as lines:
        print(part1(lines))
    print(part2())


if __name__ == '__main__':
    main()
