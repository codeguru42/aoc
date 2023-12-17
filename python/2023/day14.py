from collections import Counter

example = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


def calc_group(group, start):
  counts = Counter(group)
  return sum(range(start - counts["O"] + 1, start + 1))


def get_starts(groups, height):
  lengths = [len(group) for group in groups]
  start = height
  for length in lengths:
    yield start
    start -= length + 1


def calc_weight(column):
  height = len(column)
  groups = "".join(column).split("#")
  starts = list(get_starts(groups, height))
  weight = 0
  for group, start in zip(groups, starts):
    weight += calc_group(group, start)
  return weight


def parse(data):
  return data.splitlines()


def part1(lines):
  return sum(calc_weight(col) for col in zip(*lines))


if __name__ == '__main__':
  print(part1(parse(example)))
  with open("input.txt") as file:
    print(part1(file.readlines()))
