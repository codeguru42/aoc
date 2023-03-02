import unittest
from statistics import median


class TestDay10(unittest.TestCase):
    def test_parse_line_corrupted1(self):
        self.assertEqual(('}', None), parse_line('{([(<{}[<>[]}>{[]{[(<()>'))

    def test_parse_line_corrupted2(self):
        self.assertEqual((')', None), parse_line('[[<[([]))<([[{}[[()]]]'))

    def test_parse_line_corrupted3(self):
        self.assertEqual((')', None), parse_line('[<(<(<(<{}))><([]([]('))

    def test_parse_line_corrupted4(self):
        self.assertEqual(('}', None), parse_line('{([(<{}[<>[]}>{[]{[(<()>'))

    def test_parse_line_corrupted5(self):
        self.assertEqual(('>', None), parse_line('<{([([[(<>()){}]>(<<{{'))

    def test_parse_line_incomplete1(self):
        c, s = parse_line('[({(<(())[]>[[{[]{<()<>>')
        self.assertEqual((None, '}}]])})]'), (c, ''.join(s)))

    def test_parse_line_incomplete2(self):
        c, s = parse_line('[(()[<>])]({[<{<<[]>>(')
        self.assertEqual((None, ')}>]})'), (c, ''.join(s)))

    def test_parse_line_incomplete3(self):
        c, s = parse_line('(((({<>}<{<{<>}{[]{[]{}')
        self.assertEqual((None, '}}>}>))))'), (c, ''.join(s)))

    def test_parse_line_incomplete4(self):
        c, s = parse_line('{<[[]]>}<{[{[{[]{()[[[]')
        self.assertEqual((None, ']]}}]}]}>'), (c, ''.join(s)))

    def test_parse_line_incomplete5(self):
        c, s = parse_line('<{([{{}}[<[[[<>{}]]]>[]]')
        self.assertEqual((None, '])}>'), (c, ''.join(s)))

    def test_score_completion1(self):
        self.assertEqual(288957, score_completion('}}]])})]'))

    def test_score_completion2(self):
        self.assertEqual(5566, score_completion(')}>]})'))

    def test_score_completion3(self):
        self.assertEqual(1480781, score_completion('}}>}>))))'))

    def test_score_completion4(self):
        self.assertEqual(995444, score_completion(']]}}]}]}>'))

    def test_score_completion5(self):
        self.assertEqual(294, score_completion('])}>'))

    def test_complete1(self):
        self.assertEqual('}}]])})]', complete('[({(<(())[]>[[{[]{<()<>>'))

    def test_complete2(self):
        self.assertEqual(')}>]})', complete('[(()[<>])]({[<{<<[]>>('))

    def test_complete3(self):
        self.assertEqual('}}>}>))))', complete('(((({<>}<{<{<>}{[]{[]{}'))

    def test_complete4(self):
        self.assertEqual(']]}}]}]}>', complete('{<[[]]>}<{[{[{[]{()[[[]'))

    def test_complete5(self):
        self.assertEqual('])}>', complete('<{([{{}}[<[[[<>{}]]]>[]]'))


def parse_line(line):
    opens = '{([<'
    closes = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    s = []

    for c in line:
        if c in opens:
            s.append(c)
        else:
            d = s.pop()
            if c != closes[d]:
                return c, None
    return None, (closes[c] for c in reversed(s))


def corrupt_lines(file):
    for line in file:
        c, _ = parse_line(line.strip())
        if c:
            yield c


def part1(file):
    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    return sum(score[c] for c in corrupt_lines(file) if c)


def score_completion(rest):
    score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    total = 0
    for c in rest:
        total *= 5
        total += score[c]
    return total


def complete(line):
    _, rest = parse_line(line.strip())
    return ''.join(rest) if rest else ''


def part2(file):
    scores = (score_completion(complete(line)) for line in file)
    return median(score for score in scores if score != 0)


def main():
    with open('day10.txt') as file:
        print(part1(file))
    with open('day10.txt') as file:
        print(part2(file))


if __name__ == '__main__':
    unittest.main(exit=False)
    main()
