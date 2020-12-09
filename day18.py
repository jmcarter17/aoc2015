from utils import timer
import numpy as np


def process_line(ln):
    return [1 if i == '#' else 0 for i in ln]


def conway(data):
    copy = np.copy(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            num_on = count_on_neighbors(copy, (i, j))
            if data[i, j] == 1:
                if not 2 <= num_on <= 3:
                    data[i, j] = 0
            else:
                if num_on == 3:
                    data[i, j] = 1


def part1(data):
    for _ in range(100):
        conway(data)

    return sum(sum(data))


def part2(data):
    fix_4corners(data)
    for _ in range(100):
        conway(data)
        fix_4corners(data)

    return sum(sum(data))


def fix_4corners(data):
    for idx in [(0, 0), (0, 99), (99, 0), (99, 99)]:
        data[idx] = 1


def solve_day18(data):
    copy = np.copy(data)
    result1 = part1(data)
    result2 = part2(copy)

    return result1, result2


def count_on_neighbors(data, idx):
    x, y = idx
    xrange = range(max(0, x - 1), min(data.shape[0], x + 2))
    yrange = range(max(0, y - 1), min(data.shape[1], y + 2))

    neighbors = [(i, j) for i in xrange for j in yrange if (i, j) != idx]

    return sum(data[neighbor] for neighbor in neighbors)


@timer
def main():
    with open("inputs/day18.txt") as f:
        data = np.array([np.array(process_line(ln.strip())) for ln in f])

    print(solve_day18(data))


if __name__ == "__main__":
    main()
