from itertools import product
from math import prod
import numpy as np

from utils import timer


@timer
def four_sums_to_n(n):
    return [
        (a, b, c, n - a - b - c)
        for a in range(0, n + 1)
        for b in range(0, n + 1 - a)
        for c in range(0, n + 1 - a - b)
        if sum((a, b, c, n - a - b - c)) == n
    ]

    # return [
    #     (a, b, c, d)
    #     for a in range(0, n + 1)
    #     for b in range(0, n + 1)
    #     for c in range(0, n + 1)
    #     for d in range(0, n + 1)
    #     if sum((a, b, c, d)) == n
    # ]

    # return [comb for comb in product(range(n+1), repeat=4) if sum(comb) == n]


def process_line(ln):
    ln = ln.replace(",", "")
    items = ln.split()

    return np.array(
        [int(items[2]), int(items[4]), int(items[6]), int(items[8]), int(items[10])]
    )


def solve_day15(data):
    combs = four_sums_to_n(100)

    values1 = (prod(max(0, v) for v in np.dot(comb, data)[:-1]) for comb in combs)
    values2 = (
        prod(max(0, v) for v in np.dot(comb, data)[:-1])
        for comb in combs
        if np.dot(comb, data)[4] == 500
    )

    return max(values1), max(values2)


@timer
def main():
    with open("inputs/day15.txt") as f:
        data = np.array([process_line(ln) for ln in f])

    print(solve_day15(data))


if __name__ == "__main__":
    main()
