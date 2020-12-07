from itertools import combinations
from utils import timer


def solve_day17(data):
    combs = [
        comb
        for length in range(len(data))
        for comb in combinations(data, length)
        if sum(comb) == 150
    ]
    minlength = len(combs[0])
    return len(combs), sum(1 for x in combs if len(x) == minlength)


@timer
def main():
    with open("inputs/day17.txt") as f:
        data = sorted([int(ln.strip()) for ln in f])

    print(solve_day17(data))


if __name__ == "__main__":
    main()
