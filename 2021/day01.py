from aoc import sliding_window


def diffs(nums):
    for x, y in sliding_window(nums, 2):
        yield y - x


def three_sums(nums):
    for threes in sliding_window(nums, 3):
        yield sum(threes)


def part1():
    with open('day01.txt') as file:
        return sum(diff > 0 for diff in diffs(int(line.strip()) for line in file))


def part2():
    with open('day01.txt') as file:
        return sum(diff > 0 for diff in diffs(three_sums(int(line.strip()) for line in file)))


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
