import sys


def main():
    file = sys.argv[1]
    floor = 0
    with open(file) as fp:
        for line in fp:
            for c in line:
                if c == '(':
                    floor += 1
                elif c == ')':
                    floor -= 1
    print(floor)


if __name__ == '__main__':
    main()
