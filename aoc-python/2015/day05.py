import unittest
from collections import Counter

from itertools import islice, zip_longest


class TestHasThreeVowels(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(has_three_vowels('aei'))

    def test_example2(self):
        self.assertTrue(has_three_vowels('xazegov'))

    def test_example3(self):
        self.assertTrue(has_three_vowels('aeiouaeiouaeiou'))


class TestHasRepeatedLetter(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(has_repeated_letter('xx'))

    def test_example2(self):
        self.assertTrue(has_repeated_letter('abcdde'))

    def test_example3(self):
        self.assertTrue(has_repeated_letter('aabbccdd'))


class TestIsNice(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(is_nice('ugknbfddgicrmopn'))

    def test_example2(self):
        self.assertTrue(is_nice('aaa'))

    def test_example3(self):
        self.assertFalse(is_nice('jchzalrnumimnmhp'))

    def test_example4(self):
        self.assertFalse(is_nice('haegwjzuvuyypxyu'))

    def test_example5(self):
        self.assertFalse(is_nice('dvszwmarrgswjxmb'))


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def has_three_vowels(word):
    vowels = 'aeiou'
    count = Counter(word)
    return sum(count[v] for v in vowels) >= 3


def has_repeated_letter(word):
    for a, b in window(word):
        if a == b:
            return True
    return False


def contains_forbidden_strings(word):
    forbidden = ['ab', 'cd', 'pq', 'xy', ]
    return any(f in word for f in forbidden)


def is_nice(word):
    return (
        has_three_vowels(word) and
        has_repeated_letter(word) and
        not contains_forbidden_strings(word)
    )


def part1():
    filename = 'day05.txt'
    with open(filename) as file:
        return sum(is_nice(word) for word in file)


class TestHasRepeatingPair(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(has_repeating_pair('xyxy'))

    def test_example2(self):
        self.assertTrue(has_repeating_pair('aabcdefgaa'))

    def test_example3(self):
        self.assertFalse(has_repeating_pair('aaa'))

    def test_example4(self):
        self.assertTrue(has_repeating_pair('axyxy'))

    def test_example5(self):
        self.assertTrue(has_repeating_pair('xxyxx'))


class TestHasXYX(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(has_xyx('xyx'))

    def test_example2(self):
        self.assertTrue(has_xyx('abcdefeghi'))

    def test_example3(self):
        self.assertTrue(has_xyx('aaa'))

    def test_example5(self):
        self.assertTrue(has_xyx('xxyxx'))


class TestIsNice2(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(is_nice2('qjhvhtzxzqqjkmpb'))

    def test_example2(self):
        self.assertTrue(is_nice2('xxyxx'))

    def test_example3(self):
        self.assertFalse(is_nice2('uurcxstgmygtbstg'))

    def test_example4(self):
        self.assertFalse(is_nice2('ieodomkazucvgmuy'))


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def has_repeating_pair(word):
    for i, pair in enumerate(window(word, 2)):
        if ''.join(pair) in word[i+2:]:
            return True
    return False


def has_xyx(word):
    for triple in window(word, 3):
        if triple[0] == triple[-1]:
            return True
    return False


def is_nice2(word):
    return has_repeating_pair(word) and has_xyx(word)


def part2():
    filename = 'day05.txt'
    with open(filename) as file:
        return sum(is_nice2(word) for word in file)


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
