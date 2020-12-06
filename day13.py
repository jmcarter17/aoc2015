from itertools import permutations
from utils import timer


def get(data, p1, p2):
    if (p1, p2) not in data:
        return 0
    return data[(p1, p2)] + data[(p2, p1)]


def process_line(ln):
    src, _, gorl, num, _, _, _, _, _, _, dest = ln.split()
    num = int(num)
    if gorl == "lose":
        num = -num

    dest = dest[:-1]

    return (src, dest), num


def solve_day13(data, people):
    perms = [perm for perm in permutations(people) if perm[0] == "Alice"]
    happiness = [
        sum(get(data, *pair) for pair in zip(rank, rank[1:] + rank[0:1]))
        for rank in perms
    ]
    maximum = max(happiness)
    best = perms[happiness.index(maximum)]
    lowest_disruption = min(get(data, *pair) for pair in zip(best, best[1:] + best[0:1]))

    return maximum, maximum - lowest_disruption


@timer
def main():
    people = set()
    happypairs = {}
    with open("inputs/day13.txt") as f:
        for ln in f:
            k, v = process_line(ln)
            for p in k:
                people.add(p)
            happypairs[k] = v

    print(solve_day13(happypairs, people))


if __name__ == "__main__":
    main()
