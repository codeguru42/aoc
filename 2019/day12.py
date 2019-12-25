import re
import unittest

import numpy as np

example_moons = '''
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
'''


class TestDay12(unittest.TestCase):
    def test_parse_moons(self):
        moons = parse_moons(example_moons.strip().split('\n'))
        expected_pos = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]
        expected = [Moon(p) for p in expected_pos]
        self.assertEqual(moons, expected)

    def test_step1(self):
        moon_pos = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]
        moons = [Moon(mc) for mc in moon_pos]
        step(moons)
        expected_pos = [
            [2, -1, 1],
            [3, -7, -4,],
            [1, -7,  5,],
            [2,  2,  0,],
        ]
        expected_vels = [
            [3, -1, -1],
            [1,  3,  3],
            [-3,  1, -3],
            [-1, -3,  1],
        ]
        expected = [Moon(p, v) for p, v in zip(expected_pos, expected_vels)]
        self.assertEqual(moons, expected)


class Moon:
    def __init__(self, pos, vel=None):
        self.pos = np.array(pos)
        if vel:
            self.vel = np.array(vel)
        else:
            self.vel = np.array((0, 0, 0))

    def __eq__(self, other):
        return np.all(self.pos == other.pos) and np.all(self.vel == other.vel)

    def __str__(self):
        return f'<Moon: pos={self.pos}, vel{self.vel}>'

    def __repr__(self):
        return str(self)


def parse_moons(file):
    moons = []
    for line in file:
        matches = re.search(r'<x=(-?[0-9]+), ?y=(-?[0-9]+), ?z=(-?[0-9]+)>', line)
        moon = tuple(int(n) for n in matches.group(1, 2, 3))
        moons.append(Moon(moon))
    return moons


def compare(a, b):
    if a < b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def step(moons):
    for m1 in moons:
        for m2 in moons:
            dv = np.array([compare(a, b) for a, b in zip(m1.pos, m2.pos)])
            m1.vel += dv
    for m in moons:
        m.pos += m.vel


def calc_energy(moons):
    energy = 0
    for moon in moons:
        energy += np.sum(np.abs(moon.pos)) * np.sum(np.abs(moon.vel))
    return energy


def part1(moons):
    for _ in range(1000):
        step(moons)
    return calc_energy(moons)


def part2(moons):
    pass


def main():
    with open('day12.txt') as file:
        moons = parse_moons(file)
        print(part1(moons))
        print(part2(moons))


if __name__ == '__main__':
    main()
