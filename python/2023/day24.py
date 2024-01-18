import itertools
import timeit
from dataclasses import dataclass

import numpy as np
import numpy.typing
import pytest
from aocd import get_data

example = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""


@pytest.fixture
def lines():
    return list(parse(example))


@pytest.fixture
def line_pairs(lines):
    return itertools.combinations(lines, 2)


def test_intersection(line_pairs):
    for l1, l2 in line_pairs:
        result1 = intersection(l1, l2)
        result2 = intersection(l2, l1)
        assert np.allclose(result1[:2], result2[:2])


def test_part1():
    lines = list(parse(example))
    assert part1(lines, 7, 27) == 2


@dataclass
class Line:
    point: numpy.typing.ArrayLike
    vector: numpy.typing.ArrayLike

    def get_point(self, t):
        return self.point + t * self.vector

    def gen_points(self):
        t = 0
        while True:
            yield self.get_point(t)
            t += 1


def parse(data):
    lines = data.splitlines()
    for line in lines:
        p, v = line.strip().split("@")
        point = tuple(int(x.strip()) for x in p.strip().split(","))
        vector = tuple(int(x.strip()) for x in v.strip().split(","))
        yield Line(point=np.array(point), vector=np.array(vector))


def bounds(lbound, ubound):
    def f(x):
        return lbound <= x <= ubound

    return f


def intersection(l1: Line, l2: Line):
    a = np.column_stack((l1.vector[:2], -l2.vector[:2]))
    b = (l2.point - l1.point)[:2]
    t, s = np.linalg.solve(a, b)

    return t, s, l1.get_point(t)


def intersections(lines):
    for l1, l2 in itertools.combinations(lines, 2):
        try:
            yield intersection(l1, l2)
        except:
            pass


def part1(lines, lbound, ubound):
    in_bounds = bounds(lbound, ubound)
    return len(
        [
            (x, y)
            for t, s, (x, y, z) in intersections(lines)
            if in_bounds(x) and in_bounds(y) and t > 0 and s > 0
        ]
    )


def is_colinear(p1, p2, p3):
    v1 = p2 - p1
    v2 = p3 - p2
    return np.dot(v1, v2) != np.linalg.norm(v1) * np.linalg.norm(v2)


def part2(lines):
    pass


def main():
    data = get_data(year=2023, day=24)
    parsed = list(parse(data))
    print(parsed)
    print(
        "Part 1:",
        timeit.timeit(
            lambda: print(part1(parsed, 200000000000000, 400000000000000)),
            number=1,
        ),
    )
    print("Part 2:", timeit.timeit(lambda: print(part2(parsed)), number=1))


if __name__ == "__main__":
    main()
