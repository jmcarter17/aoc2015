from itertools import combinations
from math import prod

from utils import timer


def compute_qe(data, num_groups):
    total = sum(data)
    groupsum = total // num_groups
    combs = []
    size = 0
    while len(combs) == 0:
        size += 1
        combs = [comb for comb in combinations(data, size) if sum(comb) == groupsum]

    scombs = sorted(combs, key=prod)
    return prod(scombs[0])


@timer
def main():
    with open("inputs/day24.txt") as f:
        data = sorted([int(ln.strip()) for ln in f], reverse=True)

    part1 = compute_qe(data, 3)
    part2 = compute_qe(data, 4)

    print(part1, part2)


if __name__ == "__main__":
    main()
