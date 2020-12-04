import sys
from itertools import permutations

from utils import timer


def get(city1, city2, data):
    if (city1, city2) in data:
        return data[(city1, city2)]
    return data[(city2, city1)]


@timer
def solve_day9(data, cities):
    longest = 0
    shortest = sys.maxsize

    for items in permutations(cities):
        dist = sum(get(x, y, data) for x, y in zip(items, items[1:]))
        shortest = min(shortest, dist)
        longest = max(longest, dist)

    return shortest, longest


def main():
    with open("inputs/day9.txt") as f:
        distances = {}
        cities = set()
        for line in f:
            source, _, dest, _, dist = line.split()
            cities.add(source)
            cities.add(dest)
            distances[(source, dest)] = int(dist)

    print(solve_day9(distances, cities))


if __name__ == "__main__":
    main()
